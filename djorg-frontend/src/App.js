import React from 'react';
import NoteList from './NoteList'

import axios from 'axios';

import SignIn from './SignIn'

const ROOT_URL = 'http://localhost:8000/api'

class App extends React.Component {
  state = {
    notes: [],
    authenticated: false,
  }
  
  requestHeader = {
    headers: {
      Authorization: `Token ${localStorage.getItem('token')}`
    }
  };

  componentDidMount = async _ => {
    if (localStorage.getItem('token')) {
      this.setState({
        authenticated: true,
      });
      await this.getNotes();
    } else {
      this.setState({
        authenticated: false,
      });
    };
  };

  authenticate = async _ => {
    this.requestHeader = {
      headers: {
        Authorization: localStorage.getItem('token'),
      },
    };
    this.setState({
      authenticated: true,
    });
    await this.getNotes();
  };

  deauthenticate = _ => {
    this.setState({
      authenticated: false,
      notes: [],
    });
  };

  getNotes = async _ => {
    try {
      const res = await axios.get(`${ROOT_URL}/notes/`, this.requestHeader);
      if (res.status === 200) {
        return this.setState({
          notes: [...res.data],
        });
      };
    } catch (err) {
      return console.error(err);
    };
  };

  render() {
    return (
      <div>
        {this.state.authenticated ? (<NoteList notes={this.state.notes} />) : <SignIn ROOT_URL={ROOT_URL} axios={axios} authenticate={this.authenticate}/>}
      </div>
    )
  }
}

export default App;