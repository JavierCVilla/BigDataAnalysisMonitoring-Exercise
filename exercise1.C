#include "TFile.h"
#include "TH1F.h"
#include "TTreeReader.h"
#include "TTreeReaderValue.h"

void exercise1() {
   // Create a histogram for the values we read.
   auto myHist = new TH1F("h1","Histogram Exercise 1",100,-4,4);
   
   // Define filename and tree to be read
   auto filename = "exercise1.root";
   auto treename = "myTree";

   // Open the file containing the tree.
   auto myFile = TFile::Open(filename);
   if (!myFile || myFile->IsZombie()) {
      return;
   }
   // Create a TTreeReader for the tree, for instance by passing the
   // TTree's name and the TDirectory / TFile it is in.
   TTreeReader myReader(treename, myFile);
   // The branch "px" contains floats; access them as myPx.
   TTreeReaderValue<Double_t> myPx(myReader, "px");
   // The branch "py" contains floats, too; access those as myPy.
   TTreeReaderValue<Double_t> myPy(myReader, "py");
   // Loop over all entries of the TTree or TChain.
   while (myReader.Next()) {
      // Just access the data as if myPx and myPy were iterators (note the '*'
      // in front of them):
      myHist->Fill(*myPx + *myPy);
   }
   myHist->Draw();
}
