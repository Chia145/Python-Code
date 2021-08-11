import React from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity, TouchableNativeFeedback } from 'react-native';
import {RFValue} from 'react-native-responsive-fontsize';
import axios from 'axios'
import { Header, Icon, AirbnbRating} from 'react-native-elements';

export default class Recommend extends React.Component{

    constructor(props){
        super(props)
        this.state = {
           articleDetails : []
        }
    } 
    getArticle = () => {
        const url = 'http://ff86473978c8.ngrok.io/recommend'
        axios.get(url).then(async res => {
            let details = res.data.data
            this.setState({
                'articleDetails' : details
            })
        }).catch(e => {console.log(e.meassage)}) 
    }

    componentDidMount(){
        this.getArticle()
    }

    keyExtractor = (item, index) => {
        index.toString()
    }

    renderItems = ({item, index}) => {
        return(
            <Card 
            key = {'card-${index}'}
            image = {{uri:posterLink}}
            imageProps = {{resizeMode:'cover'}}
            featuredTitleStyle = {{color:'white', alignSelf: 'flex-start', paddingLeft: RFValue(15), fontSize: RFValue(25), marginTop: RFValue(65)}}
            featuredTitle = {item.title}
            containerStyle = {{flex: 1, borderRadius: RFValue(10), marginBottom: RFValue(20), justifyContent: 'center', height:RFValue(110)}}
            featuredSubtitle = {`${item.releaseDate.split('-')[0]} | ${this.timeConversion(item.duration)}`}
            featuredSubtitleStyle = {{fontWeight:'bold', color:'white', alignSelf: 'flex-start', paddingLeft: RFValue(15), fontSize: RFValue(15)}}
            >
                
            </Card>
        )
    }

    render(){
        return (
            <View style={styles.container}>
               <FlatList 
               data = {this.state.movieDetails} 
               keyExtractor = {this.keyExtractor} 
               renderItem = {this.renderItems}/>
            </View>
          );
    }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});