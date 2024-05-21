import React from "react"
import { Image } from "expo-image";
import {Picker, PickerIOS} from '@react-native-picker/picker';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Button } from 'react-native'; 
import DMS from './picture/DMS.png'


export default function App(){

  const [value, unChangedOutputValue] = React.useState('---');
  const [inputValue, unChangedinputValue] = React.useState('                    --Input Value Here--');
  const [inputCase, setInputCase] = React.useState('Select Case');
  const blurhash =
  '|rF?hV%2WCj[ayj[a|j[az_NaeWBj@ayfRayfQfQM{M|azj[azf6fQfQfQIpWXofj[ayj[j[fQayWCoeoeaya}j[ayfQa{oLj?j[WVj[ayayj[fQoff7azayj[ayj[j[ayofayayayj[fQj[ayayj[ayfjj[j[ayjuayj[';

  function convertValue(value) {

    if (inputCase == "1" ) {
      var degrees = Math.floor(value)
      var minutes = (Math.floor(value-degrees)*60)
      var minutes_fractional = Math.floor(minutes)
      var seconds = ((minutes - minutes_fractional) * 60)

      var output = degrees.toString().concat("-", minutes.toString(),"-", seconds.toString()) 
      unChangedOutputValue(output)
    }
    else {
      var elements = value.split('-')
      var output = parseInt(elements[0]) + (parseInt(elements[1]/60)) + (parseFloat(elements[2]/3600))%360
      unChangedOutputValue(output)
    }
    } 

  return (
    <View style={styles.Box}>
    
      <View style={styles.Title}>
        <Text style={{'fontSize' : '28' , 'fontWeight': '600', 'fontFamily' : 'Georgia', 'fontStyle' : 'italic', 'color' : '#f5ebe9'}}>D-Calculator</Text>
        <Text style={{'fontSize' : '10' , 'fontWeight': '400', 'fontFamily' : 'Georgia', 'fontStyle' : 'italic', 'color' : '#f5ebe9', 'alignContent' : 'justify'}}>-------------------------------------------------------------------------------------------------------</Text>
        <Text style={{'fontSize' : '10' , 'fontWeight': '400', 'fontFamily' : 'Georgia', 'fontStyle' : 'italic', 'color' : '#f5ebe9', 'alignContent' : 'justify'}}></Text>
        <Text style={{'fontSize' : '9' , 'fontWeight': '400', 'fontFamily' : 'Georgia', 'fontStyle' : 'italic', 'color' : '#f5ebe9', 'alignContent' : 'justify'}}>Welcome to D Calculator! </Text>
        <Text style={{'fontSize' : '8' , 'fontWeight': '400', 'fontFamily' : 'Georgia', 'fontStyle' : 'italic', 'color' : '#f5ebe9', 'alignContent' : 'justify'}}>A simple application to convert your Degree-minutes-seconds data to Decimal Degree and vice versa. </Text>
      </View>

      <View style={styles.Input1}>
        <View style={styles.TopInput}>
          <Text style = {{'fontSize' : '16' , 'fontWeight': '500' }}> INPUT CASE: </Text>
          <Picker
            style = {{postion: 'absolute', top: 0, justifyContent: 'center'}}
            selectedValue={inputCase}
            onValueChange={(itemValue, itemIndex) => {
              setInputCase(itemValue)
          }}>
          <Picker.Item label="DD To DMS" value="1" />
          <Picker.Item label="DMS To DD" value="2" />
          </Picker>
                
        </View> 

        <View style={styles.BottomInput}>
          <TextInput
          style={styles.input}
          onChangeText={unChangedinputValue}
          value={inputValue}
          /> 
          <Button
            style = {{'borderColor' : '#010200', 'borderWidth': '2', 'fontColor' : '#010200' }}
            title = "CONVERT"
            onPress={() => convertValue(inputValue)}
            />
        </View>
      </View>

      <View style={styles.Output}>
        <Text style={{'fontSize' : '24' , 'fontWeight': '600' , 'justifyContent' : 'center', 'color' : '#f5ebe9'}}> Output:</Text>
        <Text style={{'fontSize' : '24' , 'fontWeight': '600', 'color' : '#f5ebe9' }}> {value} </Text>
      </View>

      <View style={styles.box4}> 
        <Image
          style={styles.image}
          source={DMS}  
          placeholder={{ blurhash }}
          contentFit="cover"
          transition={1000}
        />
      </View>
    </View>
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
  Input1: { 
    width : '100%',
    height: '25%',
    background: 'pink',
    alignItems: 'center' , 
    justifyContent: 'center'

  },
  TopInput: { 
    flexDirection: 'column',  
    position: 'static',
    paddingtop: 20,
    width: '97%',
    height: '50%',
    backgroundColor: '#edd6c6',
    borderWidth: 2,
    borderColor: '#010200',
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

  box4: { 
    width : '100%',
    height: '40%',
    background: 'white',
    alignItems: 'center' , 
    justifyContent: 'center',
  },
  image: {
    flex: 1,
    width: '100%',
    backgroundColor: '#0553',
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

