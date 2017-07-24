//================================================================================//
// Copyright 2009 Google Inc.                                                     //
//                                                                                // 
// Licensed under the Apache License, Version 2.0 (the "License");                //
// you may not use this file except in compliance with the License.               //
// You may obtain a copy of the License at                                        //
//                                                                                //
//      http://www.apache.org/licenses/LICENSE-2.0                                //
//                                                                                //
// Unless required by applicable law or agreed to in writing, software            //
// distributed under the License is distributed on an "AS IS" BASIS,              //
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.       //
// See the License for the specific language governing permissions and            //
// limitations under the License.                                                 //
//================================================================================//
//
// sf-data-set.cc
//
// Author: D. Sculley, December 2008
// dsculley@google.com or dsculley@cs.tufts.edu
//
// Implementation of sf-data-set.h

#include <assert.h>
#include <cstdlib>
#include <iostream>
#include <fstream>

#include "sf-data-set.h"

//----------------------------------------------------------------//
//------------------ SfDataSet Public Methods --------------------//
//----------------------------------------------------------------//

SfDataSet::SfDataSet(bool use_bias_term)
  : use_bias_term_(use_bias_term) {
}

string SfDataSet::AsString() const {
  string out_string;
  for (unsigned long int i = 0; i < vectors_.size(); ++i) {
    out_string += VectorAt(i).AsString() + "\n";
  }
  return out_string;
}

const SfSparseVector& SfDataSet::VectorAt(long int index) const {
  assert (index >= 0 &&
	  static_cast<unsigned long int>(index) < vectors_.size());
  return vectors_[index];
}

void SfDataSet::AddLabeledVector(const SfSparseVector& x, float y) {
  vectors_.push_back(x);
}

void SfDataSet::ModifyLabeledVector(int idx, const SfSparseVector& x, float y) {
  vectors_[idx] = x;
}
