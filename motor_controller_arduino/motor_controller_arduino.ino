const int DIR = 8;
const int PUL = 9;
const int LED = LED_BUILTIN;


volatile bool motorActive = false;
unsigned long lastToggleTime = 0;
unsigned long pwmInterval = 10000;
bool pwmState = false;


String commandBuffer = "";
int commandCounter = 0;

void setup() {
  
  Serial.begin(9600);

  pinMode(DIR, OUTPUT);
  pinMode(PUL, OUTPUT);
  pinMode(LED, OUTPUT);
  
  digitalWrite(DIR, LOW);
  digitalWrite(PUL, LOW);
  digitalWrite(LED, LOW);
  
}

void processCommand(String command) {
  Serial.println(command);

  if (command == "MOTORSTART") {
    Serial.println("ACKMOTORSTART");
    commandCounter ++;
    if (commandCounter >= 2) {
      motorActive = true;
      commandCounter = 0;
    }
  } else if (command == "MOTORSTOP"){
    Serial.println("ACKMOTORSTOP");
    commandCounter ++;
    if (commandCounter >= 2) {
      motorActive = false;
      digitalWrite(PUL, LOW);
      digitalWrite(LED, LOW); 
      pwmInterval = 10000;
      commandCounter = 0;
    }    
  } else if (command.startsWith("SETFREQ ")) {
    String valueStr = command.substring(8);
    unsigned long newFreq = valueStr.toInt();

    if (newFreq > 10 && newFreq <= 10000) {
      Serial.print("ACKSETFREQ ");
      Serial.println(pwmInterval);
      commandCounter ++;
      if (commandCounter >= 2) {
        pwmInterval = newFreq;
        commandCounter = 0;
      }      
    }  
  
  } else {
    Serial.println(command);
  }

}

void serialHandler() {
  while (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '\n'){
      String commandSending = commandBuffer;
      commandBuffer = "";
      processCommand(commandSending);
      // commandBuffer = "";
    } else {
      commandBuffer += c;
    }
  }
}

void motorHandler() {
  if (motorActive) {
    unsigned long currentTime = micros();
    if (currentTime - lastToggleTime >= pwmInterval) {
      lastToggleTime = currentTime;
      pwmState = ! pwmState;
      digitalWrite(PUL, pwmState);
      digitalWrite(LED, pwmState);
    }
  }
}

void loop() {
  serialHandler();
  motorHandler();
}
