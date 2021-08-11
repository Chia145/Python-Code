import React from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity, TouchableNativeFeedback } from 'react-native';
import {RFValue} from 'react-native-responsive-fontsize';
import axios from 'axios'
import { Header, Icon, AirbnbRating} from 'react-native-elements';

export default class Home extends React.Component{

    constructor(){
        super()
        this.state = {
            'movieDetails' : {}
        }
    }

    getMovie = () => {
        const url = 'http://31d03fac61cf.ngrok.io/movies'
        axios.get(url).then(res => {
            let details = res.data.data
            details['duration'] = this.timeConversion(details.duration)
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

    likedMovie = () => {
        const url = 'http://31d03fac61cf.ngrok.io/liked'
        axios.post(url).then(res => {
            this.getMovie()
        }).catch(e => {console.log(e.meassage)}) 
    }

    unlikedMovie = () => {
        const url = 'http://31d03fac61cf.ngrok.io/unliked'
        axios.post(url).then(res => {
            this.getMovie()
        }).catch(e => {console.log(e.meassage)}) 
    } 
    
    unwatchedMovie = () => {
        const url = 'http://31d03fac61cf.ngrok.io/unwatched'
        axios.post(url).then(res => {
            this.getMovie()
        }).catch(e => {console.log(e.meassage)}) 
    }

    render(){
        return (
            <View style={styles.container}>
                <View style = {{flex:0.1}}>
                    <Header 
                    centerComponent = {{text:'Movies World', style:{color: '#fff', fontWeight: 'bold', fontSize: RFValue(18)}}}
                    rightComponent = {{icon: 'search', color:'#fff'}}
                    backgroundColor = {'#d500f9'}
                    containerStyle = {{flex:1}}
                    />
                </View>
                <View style = {styles.subContainer}>
                    <View style = {styles.subTopContainer}>
                        <Image 
                        style = {styles.poster}
                        source = {{uri: posterLink}}
                        />
                    </View>
                    <View style = {styles.subBottomContainer}>
                        <View style = {styles.upperBottomContainer}>

                        </View>
                        <View style = {styles.middleBottomContainer}>

                        </View>
                        <View style = {styles.lowerBottomContainer}>

                        </View>
                    </View>
                </View>
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
