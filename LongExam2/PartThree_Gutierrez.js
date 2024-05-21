import React from "react"
import { StyleSheet, Text, TextInput, View, Button } from 'react-native';

export default function App(){

    const [azimuth, unChangedOutputValue] = React.useState('---');
    const [inputValue, unChangedinputValue] = React.useState('                    --Input Value Here--');;
  
    function convertToBearing(azimuth) {
  
        if (azimuth > 0 && azimuth < 90) {
            let azimuth_dms = azimuth
            let degree = Math.floor(azimuth)
            let minutes = (azimuth_dms - degree) * 60
            let minutes_fractional = Math.floor(minutes)
            let seconds = ((minutes - minutes_fractional) * 60)
            let br_dms = degree + "-" + (Math.floor(minutes))  + "-" + (Math.round(seconds,2))
    
            let bearing = "S" + br_dms.padStart(10) + " W"
            unChangedOutputValue(bearing) 
       } else if (azimuth > 90 && azimuth <180) {
    
            let azimuth_dms = 180 - azimuth
    
            let degree = Math.floor(azimuth_dms)
            let minutes = (azimuth_dms - degree) * 60
            let minutes_fractional = Math.floor(minutes)
            let seconds = ((minutes - minutes_fractional) * 60)
            let br_dms = degree + "-" + (Math.floor(minutes)) + "-" + (Math.round(seconds,2))
    
            let bearing = "N" + br_dms.padStart(10) + " W"
            unChangedOutputValue(bearing) 
       } else if (azimuth > 180 && azimuth <270) {
    
            let azimuth_dms = azimuth - 180
    
            let degree = Math.floor(azimuth_dms)
            let minutes = (azimuth_dms - degree) * 60
            let minutes_fractional = Math.floor(minutes)
            let seconds = ((minutes - minutes_fractional) * 60)
            let br_dms = degree + "-" + (Math.floor(minutes)) + "-" + (Math.round(seconds,2))
    
            let bearing = "N" + br_dms.padStart(10) + " E"
            unChangedOutputValue(bearing)
       } else if (azimuth > 270 && azimuth <360){
            let azimuth_dms = 360 - azimuth
    
            let degree = Math.floor(azimuth_dms)
            let minutes = (azimuth_dms - degree) * 60
            let minutes_fractional = Math.floor(minutes)
            let seconds = ((minutes - minutes_fractional) * 60)
            let br_dms = degree+ "-" + (Math.floor(minutes))+ "-" + (Math.round(seconds,2))
    
            let bearing = "S" + br_dms.padStart(10) + " E"
            unChangedOutputValue(bearing)
       } else if (azimuth == 0){
            return"   DUE SOUTH  "
       } else if (azimuth == 90) {
            return "   DUE WEST  "
       } else if (azimuth == 180) {
            return "   DUE NORTH  "
       } else if (azimuth == 270) {
            return "   DUE EAST  "
       } else {
            return "Please input an azimuth value."
       }};


    return (
        <><><View style={styles.Box}>

        </View>
            <View style={styles.Title}>
                <Text style={{ 'fontSize': '28', 'fontWeight': '600', 'fontFamily': 'Georgia', 'fontStyle': 'italic', 'color': '#f5ebe9' }}>AB-Calculator</Text> 
            </View></>
            <View style={styles.BottomInput}>
                <TextInput //FOR INPUTTING TEXT
                    style={styles.input}
                    onChangeText={unChangedinputValue}
                    value={inputValue} />
                <Button //BUTTON FOR CONVERSION
                    style={{ 'borderColor': '#010200', 'borderWidth': '2', 'fontColor': '#010200' }}
                    title="CONVERT"
                    onPress={() => convertToBearing(inputValue)} />
            </View>
            <View style={styles.Output}>
                <Text style={{ 'fontSize': '24', 'fontWeight': '600', 'justifyContent': 'center', 'color': '#f5ebe9' }}> Output:</Text>
                <Text style={{ 'fontSize': '24', 'fontWeight': '600', 'color': '#f5ebe9' }}> {azimuth} </Text>
            </View></>
    );
}

const styles = StyleSheet.create({
  Box: { 
    flex: 1,
    backgroundColor: '#f5ebe9',
    alignItems: 'center' , 
    justifyContent: 'center',
  },
  Title: { 
    width : '100%',
    height: '15%',
    backgroundColor: '#010200',
    alignItems: 'center' , 
    justifyContent: 'center',
  },
  BottomInput: { 
    width: '100%',
    height: '50%',
    borderWidth: 6,
    borderColor: '#f5ebe9',
    backgroundColor: '#eaa03e',
  },
  Output: { 
    width : '97%',
    height: '20%',
    borderWidth: 2,
    borderColor: '#010200',
    backgroundColor: '#e66a47',
    alignItems: 'center' , 
    justifyContent: 'center',
  },
  input: { 
    height: '50%',
    width: '100%',
    fontSize: 22,
    color: '#010200',
    borderWidth: 2,
    borderColor: '#010200',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#60b376',
    fontFamily: 'Sans-serif'
  },
  });

  // We can improve this app further by adding a picker (A dropdown box) to be able to widen the choices of the user when converting azimuth to bearing. Instead of only having the option of DMS-DMS we could create several scenarios such as Azimuth to bearing (DD TO DMS), azimuth to bearing (DD TO DD) or Bearing to azimuth.
  // This could be implemented by importing the picker from react native then modify the picker.label to the mentioned choices then add to the function ConvertValue the code for theconverion of the said processes(Bearing to azimuth, DD TO DMS, DD TO DD, DMS TO DD).
  // For the interface of the app, it would be good if there was a home page wherein the dropbox of choices will be displayed. After choosing, the user would be redirected to another page where the values to be converted, the converted values and other GUI elements are seen. 
  // Also, adding a back to home button would be hellpful for instances where the user needs different options of conversion.
 // With this kind of interface, the user won't be overwhelmed by the amount of elements the app will displaying upon opening the app. 
