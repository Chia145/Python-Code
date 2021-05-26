import * as React from 'react';
import { Button, View, Image, Platform } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';

export default class Camera extends React.Component {
  state = {
    image: null,
  };

  pickImage = async () => {
    try {
      let result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.All,
        allowsEditing: true,
        aspect: [1, 1],
        quality: 1,
      });
      if (!result.cancelled) {
        this.setState({
          image: result.data,
        });
        this.uploadImage(result.uri);
      }
    } catch (e) {
      console.log(e);
    }
  };

  uploadImage = async (uri) => {
    const data = new FormData();
    let fileName = uri.split('/')[uri.split('/').length - 1];
    let type = `image/${uri.split('/')[uri.split('/').length - 1]}`;
    const fileToUpload = { uri: uri, name: fileName, type: type };
    data.append('digit', fileToUpload);
    fetch('https', {
      method: 'POST',
      body: data,
      headers: { 'Content-type': 'multipart/form-data' },
    })
      .then((r) => {
        r.json();
      })
      .then((result) => {
        console.log('Success:', result);
      });
  };

  getPremission = async () => {
    if (Platform.OS !== 'web') {
      const { status } = await Permissions.askAsync(Permissions.CAMERA_ROLL);
      if (status !== 'granted') {
        alert('Please allow camera to use the application.');
      }
    }
  };

  componentDidMount() {
    this.getPremission();
  }

  render() {
    return (
      <View>
        <Button title="Pick an Image" onPress={() => this.pickImage()} />
      </View>
    );
  }
}
