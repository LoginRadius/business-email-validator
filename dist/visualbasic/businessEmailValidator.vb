Imports System
Imports System.Collections.Generic
Imports System.IO
Imports System.Net.Mail
Imports Newtonsoft.Json
Imports System.Runtime.InteropServices

Namespace BusinessEmailValidator
    Public Class EmailValidator
        Public Shared Function LoadJson() As Dictionary(Of String, Boolean)
            Dim domainListItems As Dictionary(Of String, Boolean) = Nothing

            Using r As StreamReader = New StreamReader("src\freeEmailService.json")
                Dim json As String = r.ReadToEnd()
                domainListItems = JsonConvert.DeserializeObject(Of Dictionary(Of String, Boolean))(json)
            End Using

            Return domainListItems
        End Function

        Public Shared Function CheckFreeEmailDomain(ByVal emailId As String, <Out> ByRef [error] As String) As Boolean
            [error] = "Not a free email domain"

            Try
                Dim emailDomain = New MailAddress(emailId).Host
                Dim domainList = LoadJson()

                For Each domain In domainList

                    If emailDomain.ToLower() = domain.Key.ToLower() Then
                        [error] = "Free email domain"
                        Return True
                    End If
                Next

            Catch __unusedFormatException1__ As FormatException
                [error] = "Not a valid email address"
                Return False
            End Try

            Return False
        End Function
    End Class
End Namespace
