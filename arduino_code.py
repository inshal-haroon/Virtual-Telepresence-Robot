#include "arduino_secrets.h"
/* 





  bool backward;
  bool camera;
  bool forward;
  bool left;
  bool right;
*/

#include "thingProperties.h"

void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
  // This delay gives the chance to wait for a Serial Monitor without blocking if none is found
  delay(1500); 
pinMode (D0, OUTPUT);
  pinMode (D2, OUTPUT);
  pinMode (D7, OUTPUT);
  pinMode (D5, OUTPUT);
  pinMode (D8, OUTPUT);
  
  digitalWrite (D0, LOW);
  digitalWrite (D2, LOW);
  digitalWrite (D7, LOW);
  digitalWrite (D5, LOW);
   digitalWrite (D8, LOW);
  // Defined in thingProperties.h
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  
  /*
     The following function allows you to obtain more information
     related to the state of network and IoT Cloud connection and errors
     the higher number the more granular information youâ€™ll get.
     The default is 0 (only errors).
     Maximum is 4
 */
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();
  // Your code here 
  
  
}

/*
  Since Camera is READ_WRITE variable, onCameraChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onCameraChange()  {
  // Add your code here to act upon Camera change
  if (camera==1)
  {
    digitalWrite (D8, LOW);
  }
  else
  {
    digitalWrite (D8, HIGH);
  }
}
/*
  Since Forward is READ_WRITE variable, onForwardChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onForwardChange()  {
  // Add your code here to act upon Forward change
 if (forward==1)
  {
   
    digitalWrite (D0, LOW);
    digitalWrite (D2, HIGH);
    digitalWrite (D5, LOW);
    digitalWrite (D7, HIGH);
    
  }
  else
  {
digitalWrite (D0, LOW);
  digitalWrite (D2, LOW);
  digitalWrite (D7, LOW);
  digitalWrite (D5, LOW);
  }

}
/*
  Since Left is READ_WRITE variable, onLeftChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onLeftChange()  {
  // Add your code here to act upon Left change
  if (left==1)
  {
   digitalWrite (D0, LOW);
    digitalWrite (D2, HIGH);
    digitalWrite (D7, LOW);
    digitalWrite (D5, HIGH);
    
  }
  else
  {
digitalWrite (D0, LOW);
  digitalWrite (D2, LOW);
  digitalWrite (D7, LOW);
  digitalWrite (D5, LOW);
  }

}
/*
  Since Reverse is READ_WRITE variable, onReverseChange() is
  executed every time a new value is received from IoT Cloud.
*/
/*
  Since Right is READ_WRITE variable, onRightChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onRightChange()  {
  // Add your code here to act upon Right change
  if (right==1)
  {
   digitalWrite (D0, HIGH);
    digitalWrite (D2, LOW);
    digitalWrite (D7, HIGH);
    digitalWrite (D5, LOW);
    
  }
  else
  {
  digitalWrite (D0, LOW);
  digitalWrite (D2, LOW);
  digitalWrite (D7, LOW);
  digitalWrite (D5, LOW);
  }

}

/*
  Since Backward is READ_WRITE variable, onBackwardChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onBackwardChange()  {
  // Add your code here to act upon Backward change
     if (backward==1)
  {
   
    digitalWrite (D2, LOW);
    digitalWrite (D0, HIGH);
    digitalWrite (D7, LOW);
    digitalWrite (D5, HIGH);
    
  }
  else
  {
  digitalWrite (D0, LOW);
  digitalWrite (D2, LOW);
  digitalWrite (D7, LOW);
  digitalWrite (D5, LOW);
  }
}