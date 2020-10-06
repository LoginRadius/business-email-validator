package com.loginradius

import com.beust.klaxon.Klaxon
import java.util.regex.Pattern

object EmailValidator {
    private const val expression = "^[\\w.-]+@(?<domain>[\\w\\-]+\\.)+[A-Z]{2,8}$"

    private val domains = Klaxon().parse<Map<String,Boolean>>(
            this.javaClass.classLoader.getResourceAsStream("list.json")!!)?.keys ?: emptySet()

    fun isEmailValid(address: String) : Boolean {
        val pattern = Pattern.compile(expression, Pattern.CASE_INSENSITIVE)
        val matcher = pattern.matcher(address)
        //Check if it's an actual email
        if (!matcher.matches()){
            return false
        }
        val domain = matcher.group("domain")
        return domain.toLowerCase() !in domains
    }
}

