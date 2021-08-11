import React from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity, TouchableNativeFeedback } from 'react-native';
import {RFValue} from 'react-native-responsive-fontsize';
import axios from 'axios'
import { Header, Icon, AirbnbRating} from 'react-native-elements';

export default class Recommend extends React.Component{

    constructor(){
        super()
        this.state = {
           movieDetails : []
        }
    } 
    getMovie = () => {
        const url = 'http://31d03fac61cf.ngrok.io/recommend'
        axios.get(url).then(async res => {
            let details = res.data.data
            this.setState({
                'movieDetails' : details
            })
        }).catch(e => {console.log(e.meassage)}) 
    }

    componentDidMount(){
        this.getMovie()
    }

    timeConversion = (n) => {
        var h = Math.floor(n/60)
        var m = n % 60
        return `${h} hrs ${m} mins`
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