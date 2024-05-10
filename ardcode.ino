#define ledPin1 4 // Define GPIO pin for LED 1
#define ledPin2 5 // Define GPIO pin for LED 2
#define ledPin3 6 // Define GPIO pin for LED 3
#define inputpin 3
void isr(){
    Serial.println("3");
}

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud rate
  pinMode(ledPin1, OUTPUT); // Set LED pin as output
  pinMode(ledPin2, OUTPUT); // Set LED pin as output
  pinMode(ledPin3, OUTPUT); // Set LED pin as output
  pinMode(inputpin,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(inputpin),isr,FALLING);
  digitalWrite(ledPin1,HIGH);
}

void loop() {
  
  if (Serial.available() > 0) { // Check if data is available to read
    char command = Serial.read(); // Read the incoming byte
    
    // Check which command was received
    switch (command) {
      case '1':
        digitalWrite(ledPin1, LOW);
        digitalWrite(ledPin2,HIGH);
        delay(3000);
        digitalWrite(ledPin2,LOW);
        digitalWrite(ledPin3,HIGH);
        delay(7000);
        break;
      case '2':
        digitalWrite(ledPin1,LOW);
        digitalWrite(ledPin2, HIGH);
        delay(5000);
        break;
      default:
        break;
    }
    
  }
  digitalWrite(ledPin1,HIGH);
    digitalWrite(ledPin2,LOW);
    digitalWrite(ledPin3,LOW);
}
