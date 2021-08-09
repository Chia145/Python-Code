import React from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity, TouchableNativeFeedback } from 'react-native';
import {RFValue} from 'react-native-responsive-fontsize';
import axios from "axios";
import { Header, Icon, AirbnbRating} from 'react-native-elements';

export default class Home extends React.Component{

    constructor(){
        super()
        this.state = {
            'articleDetails' : {}
        }
    }

    getArticle = () => {
        const url = 'http://localhost:5000/movies'
        axios.get(url).then(res => {
            let details = res.data.data
            this.setState({
                'articleDetails' : details
            })
        }).catch(e => {console.log(e.meassage)}) 
    }

    componentDidMount(){
        this.getArticle()
    }

    likedArticle = () => {
        const url = 'http://localhost:5000/liked'
        axios.post(url).then(res => {
            this.getMovie()
        }).catch(e => {console.log(e.meassage)}) 
    }

    unlikedArticle = () => {
        const url = 'http://localhost:5000/unliked'
        axios.post(url).then(res => {
            this.getMovie()
        }).catch(e => {console.log(e.meassage)}) 
    } 
    
    render() {
        const { articleDetails } = this.state;
        if (articleDetails.url) {
          const { url } = articleDetails;
    
          return (
            <View style={styles.container}>
              <View style={styles.headerContainer}>
                <Header
                  centerComponent={{
                    text: "Recommended",
                    style: styles.headerTitle
                  }}
                  rightComponent={{ icon: "search", color: "#fff" }}
                  backgroundColor={"#d500f9"}
                  containerStyle={{ flex: 1 }}
                />
              </View>
              <View style={styles.upperContainer}>
                <WebView source={{ uri: url }} />
              </View>
              <View style={styles.lowerContainer}>
                <View style={styles.buttonContainer}>
                  <TouchableOpacity onPress={this.likedArticle}>
                    <Icon
                      reverse
                      name={"check"}
                      type={"entypo"}
                      size={RFValue(30)}
                      color={"#76ff03"}
                    />
                  </TouchableOpacity>
                  <TouchableOpacity onPress={this.unlikedArticle}>
                    <Icon
                      reverse
                      name={"cross"}
                      type={"entypo"}
                      size={RFValue(30)}
                      color={"#ff1744"}
                    />
                  </TouchableOpacity>
                </View>
              </View>
            </View>
          );
        }
        return null;
      }
    }
    
    const styles = StyleSheet.create({
      container: {
        flex: 1
      },
      headerContainer: {
        flex: 0.1
      },
      headerTitle: {
        color: "#fff",
        fontWeight: "bold",
        fontSize: RFValue(18)
      },
      upperContainer: {
        flex: 0.75
      },
      lowerContainer: {
        flex: 0.15
      },
      buttonContainer: {
        flexDirection: "row",
        justifyContent: "space-evenly",
        alignItems: "center"
      }
    });
