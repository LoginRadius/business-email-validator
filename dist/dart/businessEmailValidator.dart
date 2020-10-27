/// A library capable of identifying if an email is a free business one,
/// or a custom one.
library businessEmailValidator;

import 'dart:convert';
import 'dart:io';

const _JSON_PATH = '../../src/freeEmailService.json';

/// This class implement the core logic for the `businessEmailValidator` library.
///
/// It loads the dataset of valid emails, and identifies if the email
/// is valid or not through the [isValid] method
class BusinessEmailValidator {
  /// This Set will contain every invalid domain
  Set<String> _invalidDomains = {};

  /// Flag indicating if we have already loaded the data to `_invalidDomains`
  bool _initialized = false;

  /// Init function, which reads from _JSON_PATH, and loads the
  /// content to the `_invalidDomains` instance variable, for later use.
  ///
  /// Keep in mind this function is only called when the JSON with the data has
  /// not being loaded yet
  Future _init() async {
    String contents = await new File(_JSON_PATH).readAsString();
    Map<String, dynamic> jsonMap = jsonDecode(contents);

    for (String key in jsonMap.keys) {
      _invalidDomains.add(key);
    }

    _initialized = true;
  }

  /// Returns a [Future<bool>] indicating if [email] is a
  /// valid email, or a free one
  Future<bool> isValid(String email) async {
    if (!_initialized) {
      await this._init();
    }

    String domain = email.split('@').last;
    return !_invalidDomains.contains(domain);
  }
}
