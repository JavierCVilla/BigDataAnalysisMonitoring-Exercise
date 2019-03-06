import ROOT

# This script creates and fills a test tree: this makes the example stand-alone.
# Use the RDataFrame interface to create a new TTree with two branches (px, py).
# Values are randomly generated following a Gaus distributions.

# Internal options to save the tree into disk
rsops = ROOT.ROOT.RDF.RSnapshotOptions(
         "RECREATE",       # mode
         ROOT.ROOT.kZLIB,  # compression algorithm
         1,                # compression level
         200,              # autoflush, number of events per cluster
         99,               # split level of output tree
         0                 # lazy
        )

# C++ code to be injected into the C++ interpreter of ROOT
randomGausCode="""
TRandom3 R(1);

auto randomGaus = [](double min, double max){
   return R.Gaus(min, max);
};
"""

# Declare `randomGaus` so it can be use later on
ROOT.gInterpreter.Declare(randomGausCode)

# Create ROOT file with 300000 events and 2 branches (columns)
def fill_tree(treeName, fileName):
   rdf = ROOT.ROOT.RDataFrame(300000)
   rdf.Define("px", "randomGaus(0.,10.)")\
      .Define("py", "randomGaus(0.,10.)")\
      .Snapshot(treeName, fileName, "", rsops)
 
# We prepare an input tree to run on
fileName = "exercise1.root"
treeName = "myTree"
fill_tree(treeName, fileName)

