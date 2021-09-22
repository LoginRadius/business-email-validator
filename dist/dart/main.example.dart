import 'businessEmailValidator.dart';

main() async {
  var businessEmailValidator = new BusinessEmailValidator();

  print(await businessEmailValidator.isValid('abc@my_domain.com')); // true
  print(await businessEmailValidator.isValid('abc@iwon.com')); // false
}
