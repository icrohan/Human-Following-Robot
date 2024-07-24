
#define IN1 12
#define IN2 14
#define IN3 27
#define IN4 26
void setup() {
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n'); // Read data until newline character
    Serial.println(message);
    if(message == "Right"){
      digitalWrite(IN1,HIGH);
      digitalWrite(IN2,LOW);
      digitalWrite(IN3,LOW);
      digitalWrite(IN4,LOW);
    }
    if(message == "Left"){
      digitalWrite(IN1,LOW);
      digitalWrite(IN2,LOW);
      digitalWrite(IN3,HIGH);
      digitalWrite(IN4,LOW);
    }
    if(message == "Center"){
      digitalWrite(IN1,HIGH);
      digitalWrite(IN2,LOW);
      digitalWrite(IN3,HIGH);
      digitalWrite(IN4,LOW);
    }
  }
}