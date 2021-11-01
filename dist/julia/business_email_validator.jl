# Author : Fernanda Kawasaki
# https://github.com/fernandakawasaki

import JSON

# Function to get json dict
function load_json()
    email_list = JSON.parsefile("../../src/freeEmailService.json")
    return email_list
end

function get_domain(email)
    email_split = split(email, "@")
    if length(email_split) >= 2
        domain = last(email_split)
        return domain
    end
    return ""
end

# Function to validate email
function validate(email)
    email_list = load_json()
    domain = get_domain(email)

    # Check if email has at least one "@"
    if haskey(email_list, domain)
        return true
    end
    return false
end
