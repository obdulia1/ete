import unittest
import os
import time
from ete_dev import nexml, phyloxml
import sys

class Test_PhyloXML(unittest.TestCase):
    def test_phyloxml_parser(self):
        path = "../examples/phyloxml/"
        for fname in os.listdir(path):
            if fname.endswith(".xml"):
                W = open("/tmp/test_xml_parser", "w")
                print fname, "...", 
                fpath = os.path.join(path, fname)
                p = phyloxml.Phyloxml()
                t1 = time.time()
                p.build_from_file(fpath)
                etime = time.time()-t1
                print "%0.1f secs" %(etime)
                p.export(outfile = W)

class Test_NeXML(unittest.TestCase):
    def test_nexml_parser(self):
        path = "../examples/nexml/"
        for fname in os.listdir(path):
            if fname.endswith(".xml"):
                W = open("/tmp/test_xml_parser", "w")
                print fname, "...", 
                fpath = os.path.join(path, fname)
                p = nexml.Nexml()
                t1 = time.time()
                p.build_from_file(fpath)
                etime = time.time()-t1
                print "%0.1f secs" %(etime)
                p.export(outfile = W)



if __name__ == '__main__':
    unittest.main()