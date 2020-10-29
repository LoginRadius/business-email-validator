#include <string>
#include <iostream>

#include "json.hpp"
using json = nlohmann::json;

#include <fstream>
#include <sstream>



std::vector<std::string> split (const std::string &s, char delim) {
    std::vector<std::string> result;
    std::stringstream ss (s);
    std::string item;

    while (getline (ss, item, delim)) {
        result.push_back (item);
    }
    return result;
}

namespace wrapper {
  bool is_free(std::string email){
    std::ifstream fin("../../src/free_email_service.json");
    json domains = json::parse(fin);

    std::vector<std::string> v = split(email, '@');
    if(v.size() != 2) return false;
    return domains.find(v[1]) != domains.end();
  }
}

