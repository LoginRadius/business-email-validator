import com.loginradius.EmailValidator
import org.spekframework.spek2.Spek
import org.spekframework.spek2.style.specification.describe

object ValidatorTests : Spek( {

    describe("The validator") {
        mapOf(
            "valid@gmail.com" to true,
            "valid@yahoo.com" to true,
            "qwerty" to false,
            "asdf@asdf@asdf" to false
        ).forEach { (input, expectedResult) ->
            describe("Testing for input: $input") {
                it ("Validates to $expectedResult") {
                    assert(EmailValidator.isEmailValid(input) == expectedResult) { "Assertion Failed, verification mismatch: $input should validate to $expectedResult" }
                }
            }
        }
    }

})
