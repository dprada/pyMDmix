#!/usr/bin/env python

def init_solvent_db():

    import os
    import glob
    from . import Solvents
    path = os.path.join(os.path.dirname(Solvents.__file__), 'data','solventlib')
    print("Building solvent database...")
    dbpath = os.path.join(path, 'SOLVENTS.db')
    configfilelist = glob.glob(os.path.join(path, '*.config'))
    maker=Solvents.SolventManager()
    for conffile in configfilelist:
        print('Adding solvent from {}'.format(conffile))
        maker.saveSolvent(maker.createSolvent(conffile), db=dbpath, createEmpty=True)
    if os.path.exists(dbpath): print("DONE creating solvent DB")

