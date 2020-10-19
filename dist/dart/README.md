# BusinessEmailValidator Wrapper for Dart 🕴️

Here we have a custom and minimal wrapper for Dart, to use the BusinessEmailValidator dataset directly.

Custom driver code:

```dart
    import 'businessEmailValidator.dart';

    main() async {
    var businessEmailValidator = new BusinessEmailValidator();

    print(await businessEmailValidator.isValid('abc@my_domain.com')); // true
    print(await businessEmailValidator.isValid('abc@iwon.com')); // false
    }
```

Keep in mind that the library returns a `Future<bool>` (because of the JSON reading), so, you need to use the `await` keyword when using it.

## Author 🧙‍♂️

- RafaAudibert ➡️ [www.rafaaudibert.dev](www.rafaaudibert.dev)
