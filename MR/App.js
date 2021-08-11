import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Home from './Screens/home'
import Popular from './Screens/popular';
import Recommend from './Screens/recommend';
import { createAppContainer} from 'react-navigation';
import {createStackNavigator} from  'react-navigation-stack'
import {createMaterialTopTabNavigator} from 'react-navigation-tabs'
import {RFValue} from 'react-native-responsive-fontsize'

export default function App() {
  return (
    <Ac />
  );
}

const Atn =createMaterialTopTabNavigator({
  RecommendedMovies: {
    screen : Recommend,
    navigationOptions: {
      tabBarLabel : "Recommended",
      tabBarOptions : {
        tabStyle: {backgroundColor: 'white'},
        lableStyle: {color: 'black'},
        indicaterStyle: {backgroundColor:'black'}
      }
    }
  }, 
  PopularMovies: {
    screen : Popular,
    navigationOptions: {
      tabBarLabel : "Popular Movies",
      tabBarOptions : {
        tabStyle: {backgroundColor: 'white'},
        lableStyle: {color: 'black'},
        indicaterStyle: {backgroundColor:'black'}
      }
    }
  }
})

const Asn = createStackNavigator({
  Home: {
    screen:Home,
    navigationOptions: {headerShown: false}
  },
  Atn : {
    screen:Atn,
    navigationOptions: {
      headerBackTitle: null, 
      headerTintColor:'white', 
      headerTitle:'Recommended Movies',
      headerStyle: {backgroundColor: '#d500f9'},
      headerTitleStyle: {color: 'white', fontWeight:'bold', fontSize: RFValue(18)}
    }
  }
}, {
  intitialRouteName: 'Home'
})

const Ac = createAppContainer(Asn)

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
