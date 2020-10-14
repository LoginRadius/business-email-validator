import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import java.io.FileReader;
import java.lang.NullPointerException;

public class BusinessEmailValidator {
	public static boolean validate(String email) {
		JSONParser parser = new JSONParser();
		try {

			// Get email domain
			int domainStart = email.lastIndexOf("@");
			if (domainStart == -1) {
				return false;
			}

			String domain = email.substring(domainStart + 1).toLowerCase();

			// Open JSON file
			FileReader jsonFileReader = new FileReader("src/freeEmailService.json");
			JSONObject jsonObject = (JSONObject)parser.parse(jsonFileReader);
			jsonFileReader.close();

			return !(boolean)jsonObject.get(domain);
		} catch (NullPointerException e) {
		} catch (Exception e) {
			e.printStackTrace();
		}
		return false;
	}
}
