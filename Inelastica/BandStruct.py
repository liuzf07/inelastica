"""
Bandstructure and Fermi surface calculator
"""

import Symmetry as SYM
import SiestaIO as SIO
import MakeGeom as MG
import MiscMath as MM
import numpy as N
import numpy.linalg as LA
import sys, string, struct, glob,  os
from optparse import OptionParser, OptionGroup
import PhysicalConstants as PC
import WriteXMGR as XMGR

mm = MM.mm
outerAdd = MM.outerAdd
dist = MM.dist
mysqrt = MM.mysqrt

# Dummy classes for global variables
# general, HS, basis and geom are a global variables

########################################################
##################### Main routine #####################
########################################################
def main():
    setupParameters()

    readxv()
    readHS()
    readbasis()
    for ispin in range(HS.nspin):
        calcBands(ispin)
        calcFS(ispin)

########################################################
def readxv():
    global geom
    # Read geometry from first .XV file found in dir
    fns=glob.glob('*.XV')

    if len(fns)>1:
        print "ERROR: BandStruct: More than one .XV file ... which geometry to choose???"
        sys.exit(1)
    elif len(fns)<1:
        print "ERROR: BandStruct: Error ... No .XV file found!"
        sys.exit(1)

    print('Reading geometry from "%s" file' % fns[0])
    geom = MG.Geom(fns[0])
    geom.sym = SYM.Symmetry(fns[0],onlyLatticeSym=True)
    if geom.sym.NNbasis != geom.natoms:
        print "ERROR: Siesta cell does not contain one unit cell"
        kuk

########################################################
def readbasis():
    global basis
    fn=glob.glob('RUN.fdf')
    basis = SIO.BuildBasis(fn[0], 1, geom.sym.NN, HS.lasto)

########################################################
def readHS():
    # Setup H, S and self-energies
    global HS
    fn = glob.glob('*.TSHS')
    if len(fn)>1:
        print "ERROR: BandStruct: More than one .TSHS file ... which to choose???"
        kuk
    if len(fn)<1:
        print "ERROR: BandStruct: No .TSHS file ???"
        kuk
    HS = SIO.HS(fn=fn[0])
    

########################################################
def calcFS(ispin):
    # Calculate Fermi-surface
    NNk = general.NNk    
    bands = N.zeros((NNk,NNk,NNk,HS.N),N.float)
    for ix in range(general.NNk):
        for iy in range(general.NNk):
            for iz in range(general.NNk):
                # "unitless" k-vect
                kpnt = N.array([ix,iy,iz],N.float)/float(NNk-1)
                HS.setkpoint(kpnt)
                eval,evec = LA.eig(mm(LA.inv(HS.S),HS.H[ispin, :, :]))
                ipiv = N.argsort(eval)
                bands[ix,iy,iz,:] = eval[ipiv]
        SIO.printDone(ix,NNk,'Fermi Surface: ')
    writeFS(ispin,NNk,bands)

def writeFS(ispin, NNk, bands):
    # Write output
    if HS.nspin>1:
        sspin = ['.up','.down'][ispin]
    else:
        sspin = ''

    # How many bands to include ?
    indx = []
    for ii in range(HS.N):
        if N.sum((bands[:,:,:,ii].reshape((-1,))<general.eMax)*\
                     (bands[:,:,:,ii].reshape((-1,))>general.eMin)):
            indx += [ii]

    f = open(general.DestDir+'/'+'FermiSurface'+sspin+'.BXSF','w')
    f.write("""
BEGIN_INFO
   # Band-XCRYSDEN-Structure-File 
   # Generated by Inelastica.BandStruct
   # Launch as: xcrysden --bxsf example.bxsf
   #
   Fermi Energy: 0.0000
END_INFO
BEGIN_BLOCK_BANDGRID_3D
   What_is_this_text
   BEGIN_BANDGRID_3D_simple_example
     %i"""%len(indx))
    f.write("\n     %i %i %i\n"%(NNk,NNk,NNk))
    f.write("\n     0.0 0.0 0.0\n")
    rlat = [geom.sym.b1, geom.sym.b2, geom.sym.b3]
    f.write("\n     %f %f %f\n"%(rlat[0][0],rlat[0][1],rlat[0][2]))
    f.write("\n     %f %f %f\n"%(rlat[1][0],rlat[1][1],rlat[1][2]))
    f.write("\n     %f %f %f\n"%(rlat[2][0],rlat[2][1],rlat[2][2]))
    for ii in indx:
        f.write("\n   BAND:  %i\n"%(ii))
        for ix in range(NNk):
            for iy in range(NNk):
                for iz in range(NNk):
                    f.write('%f '%bands[ix,iy,iz,ii])
                f.write('\n')
            f.write('\n')
    f.write("""
   END_BANDGRID_3D
END_BLOCK_BANDGRID_3D
""")



########################################################
def calcBands(ispin):
    # Calculate bandstructure along high symmetry directions
    # what = [["text",k-direction, k-origin, Num k-points], ...]
    what = geom.sym.what()
    
    bands = []
    for txt, kdir, korig, Nk in what:
        ev = N.zeros((Nk,HS.N),N.float)
        for ii in range(Nk):
            kpnt = korig + kdir*(ii/float(Nk-1))
            # Change to "unitless" k-vect
            kpnt2 = mm(N.array([geom.sym.a1,geom.sym.a2,geom.sym.a3]), kpnt)

            HS.setkpoint(kpnt2)
            eval,evec = LA.eig(mm(LA.inv(HS.S),HS.H[ispin, :, :]))
            ipiv = N.argsort(eval)
            ev[ii,:] = eval[ipiv]
        bands += [ev]
    
    writeBands(ispin,what,bands)


########################################################
def writeBands(ispin,what,bands):
    # Write output
    if HS.nspin>1:
        sspin = ['.up','.down'][ispin]
    else:
        sspin = ''

    Graphs = []
    for jj,  elem in enumerate(what):
        f=open(general.DestDir+'/'+elem[0]+sspin+'.dat','w')
        xx = N.array(range(elem[3]),N.float)/(elem[3]-1.0)
        iColor, Datasets = 1, []
        for ii in range(len(bands[jj][0,:])):
            # Choose bands within +-5 eV from Ef
            if N.sum((bands[jj][:,ii]<general.eMax)*\
                         (bands[jj][:,ii]>general.eMin))>1e-5:
                f.write("\n# Band %i \n"%(ii))                
                for kk,data in enumerate(bands[jj][:,ii]):
                    f.write("%i %e\n"%(kk,data))
                Datasets += [XMGR.XYset(xx,bands[jj][:,ii],Lcolor=iColor)]
                iColor += 1
        f.close()

        g = XMGR.Graph()
        for data in Datasets:
            g.AddDatasets(data)
        g.SetSubtitle(what[jj][0])

        g.SetXaxis(label='',majorUnit=0.5,minorUnit=0.1,max=1,min=0)     
        if jj==0:
            g.SetYaxis(label='eV',majorUnit=1,minorUnit=0.2,\
                           max=general.eMax,min=general.eMin)
        else:
            g.SetYaxis(label='',majorUnit=1e10,minorUnit=0.2,\
                           max=general.eMax,min=general.eMin)
        Graphs+=[g]

    p = XMGR.Plot(general.DestDir+'/BandStruct.agr',Graphs[0])

    for ii in range(1,len(Graphs)):
        p.AddGraphs(Graphs[ii])
    p.ArrangeGraphs(nx=len(Graphs),ny=1,hspace=0.0,vspace=0.0)

    # Finally, write the plot file
    p.ShowTimestamp()
    p.WriteFile()
    p.Print2File(general.DestDir+'/BandStruct.eps')


###########################################################
def setupParameters():
    global general
    
    usage = "usage: %prog [options] DestinationDirectory"
    description = """
Calculation of Fermi surface.

For help use --help!
"""
    parser = OptionParser(usage,description=description)
    EC = OptionGroup(parser, "Options for Fermi surface")
    EC.add_option("-N", "--NumPoints", dest='NNk', default=20,type='int',
                  help="Number of k-points for Fermi-surface calculation [%default]")
    EC.add_option("-f", "--fdf", dest='fdfFile', default='./RUN.fdf',type='string',
                  help="fdf file used for transiesta calculation [%default]")
    EC.add_option("-a", "--min", dest='eMin', default=-5.0,type='float',
                  help="min of energy range to plot [%default]")
    EC.add_option("-b", "--max", dest='eMax', default=5.0,type='float',
                  help="max of energy range to plot [%default]")

    parser.add_option_group(EC)
    
    (general, args) = parser.parse_args()
    print description

    if not os.path.exists(general.fdfFile):
        parser.error("No input fdf file found, specify with --fdf=file.fdf (default RUN.fdf)")

    print args
    if len(args)!=1:
        parser.error('ERROR: You need to specify destination directory')
    general.DestDir = args[0]
    if not os.path.isdir(general.DestDir):
        print '\nBandStruct : Creating folder %s' %general.DestDir
        os.mkdir(general.DestDir)
    else:
        parser.error('ERROR: destination directory %s already exist!'%general.DestDir)

    def myprint(arg,file):
        # Save in parameter file
        print arg
        file.write(arg+'\n')

    class myopen:
        # Double stdout to RUN.out and stdout
        def write(self,x):
            self.stdout.write(x)
            self.file.write(x)

    fo = myopen()
    fo.stdout, fo.file = sys.stdout, open(general.DestDir+'/RUN.out','w',0)
    sys.stdout = fo

    file = open(general.DestDir+'/Parameters','w')    
    argv=""
    for ii in sys.argv: argv+=" "+ii
    myprint(argv,file)
    myprint('##################################################################################',file)
    myprint('## Band structure ',file)
    myprint('fdfFile            : %s'%general.fdfFile,file)
    myprint('Number of k-points : %f'%general.NNk,file)
    myprint('##################################################################################',file)
    file.close()

    
##################### Start main routine #####################

if __name__ == '__main__':
    main()

