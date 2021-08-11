import React from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity, TouchableNativeFeedback } from 'react-native';
import {RFValue} from 'react-native-responsive-fontsize';
import axios from "axios";
import { Header, Icon, AirbnbRating} from 'react-native-elements';

export default class Home extends React.Component{

constructor(props){
    super(props)
    this.state = {
        articleDetails : {}
    }
}

getArticle = () => {
    const url = 'http://ff86473978c8.ngrok.io/articles'
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
    const url = 'http://ff86473978c8.ngrok.io/liked'
    axios.post(url).then(res => {
        this.getMovie()
    }).catch(e => {console.log(e.meassage)}) 
}

unlikedArticle = () => {
    const url = 'http://ff86473978c8.ngrok.io/unliked'
    axios.post(url).then(res => {
        this.getMovie()
    }).catch(e => {console.log(e.meassage)}) 
} 
renderItem = ({item, index}) => (
  <ListItem
  key = {index}
  bottomDivider
  title = {`Article Name : ${item.title.toUpperCase()}`}
  titleStyle = {{color: '#F24C00', fontSize : 18, fontWeight: "bold"}}
  subtitle = {`Date Published : ${moment.unix(item.timestamp).format("DD/MM/YYYY")}`}
  subtitleStyle = {{color: '#FC7A1E', fontSize: 16}}
  chevron = {{color: '#F9C784', size: 25}}
  onPress = {() => {
      this.props.navigation.navigate("ViewArticle", {
          article_name: item.title.toUpperCase(),
          url: item.url,
          id: item.id
      })
  }}
  containerStyle = {{backgroundColor: '#E7E7E7'}}
  >
  </ListItem>
)
keyExtractor = (item, index) => index.toString();

render(){
  return (
      <View style={styles.container}>
        <Card
        containerStyle = {{flex: 0.1, backgroundColor: '#E7E7E7'}}>
            <Text style = {{color: '#F24C00', fontSize : 18, fontWeight: "bold"}}>Liked the article?</Text>
            <View
            style = {{
                flexDirection: 'row',
                justifyContent: 'space-around',
                marginTop: 10
            }}>
                <Pressable
                onPress = {() => {
                    this.likedArticle()
                }}>
                    <Icon name = "check" type = "feather" size = {40} color = "#15D849"/>
                </Pressable>

                <Pressable
                onPress = {() => {
                    this.unlikedArticle()
                }}>
                    <Icon name = "x" type = "feather" size = {40} color = "#F24C00"/>
                </Pressable>
            </View>
        </Card>
      </View>
    );
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
