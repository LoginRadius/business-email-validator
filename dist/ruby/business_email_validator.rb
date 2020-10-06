require 'json'

class BusinessEmailValidator
  FILE_PATH = "/../../src/freeEmailService.json"
  @@data = []

  def self.initialize()
    file = File.join(File.dirname(__FILE__), FILE_PATH)
    json = File.read(file)
    @@data = JSON.parse(json)
  end

  # @email [String] An email to be validate.
  # @return [Boolean] True or False if the domain is valide or not.
  def self.validate(email)
    return false unless (email =~ URI::MailTo::EMAIL_REGEXP).nil?.!

    if @@data.empty? then
      self.initialize()
    end

    domain = email.downcase.split("@").last
    matchDomain = @@data.find { |item| item[0] == domain }
    matchDomain.nil?
  end
end
