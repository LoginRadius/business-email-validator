<?php

class BusinessEmailValidator
{

	/**
	* Used to load list of blocked domains from local JSON file.
	* @access private
	* @return array
	*/
	private function listBlocked()
	{
		$path = 'src/freeEmailService.json';
		file_exists($path) or die("Error: file 'freeEmailService.json' not found!");
		return (array) json_decode(file_get_contents($path), true);			
	}

	/**
	* Used to check if provided email address is in list of blocked domains
	* @access public
	* @param string $email
	* The email address we want to check
	* @example 'john@doe.com'
	* @return bool
	*/
	public function isBlocked($email)
	{
		filter_var($email, FILTER_VALIDATE_EMAIL) or die("Not a valid email address!");
		$list_blocked = $this->listBlocked();
		if(is_array($list_blocked) && filter_var($email, FILTER_VALIDATE_EMAIL))
		{
			$email_domain = explode('@', $email);
		    $email_domain = end($email_domain);
		    
		    foreach ($list_blocked as $domain => $blocked)
		    {
		    	if($email_domain === $domain)
		    	{
		    		return true;
		    	}
		    }
		    return false;
		}else{
			echo "Not a valid email address!";
		}
	}
}