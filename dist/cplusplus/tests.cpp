#include <vector>
#include <string>
#include <iostream>

#include "wrapper.hpp"

using namespace std;

vector<string> test_cases_valid = {
  "valid@gmail.com",
  "valid@yahoo.com",
};

vector<string> test_cases_invalid = {
  "qwerty",
  "asdf@asdf@asdf",
};

vector<string> failed_tests;

int main(){
  cout << "starting tests..." << endl;
  
  for(const auto &test : test_cases_valid){
    if(!wrapper::is_free(test)){
      failed_tests.push_back(test);
    }
  }
  for(const auto &test : test_cases_invalid){
    if(wrapper::is_free(test)){
      failed_tests.push_back(test);
    }
  }

  cout << test_cases_valid.size() + test_cases_invalid.size() << " tests ran, " << failed_tests.size() << " tests failed." << endl;
  for(const auto &failed_test : failed_tests){
    cout << "FAIL: " << failed_test << endl;
  }
}