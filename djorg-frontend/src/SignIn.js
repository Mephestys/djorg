import React from 'react';

class SignIn extends React.Component {
  state = {
    username: '',
    password: '',
    error: null,
  };

  login = async (username, password) => {
    if (!username || !password) {
      return this.setState({
        error: 'Please input a valid username and password.'
      });
    };
    try {
      const res = await this.props.axios.post(`${this.props.ROOT_URL}-token-auth/`, { username, password });
      const token = res.data.token;
      localStorage.setItem('token', token);
      this.props.authenticate();
    } catch (err) {
      this.setState({
        error: 'Invalid username or password.'
      });
    };
  };

  handleInputChange = event => {
    event.preventDefault();
    this.setState({ [event.target.name]: event.target.value });
  };

  handleSubmit = event => {
    event.preventDefault();
    const { username, password } = this.state;
    this.login(username, password);
    this.setState({ username: '', password: '' });
  };

  renderAlert = _ => {
    if (!this.state.error) return null;
    return <h3>{this.state.error}</h3>;
  };

  render() {
    const { username, password } = this.state;

    return (
      <div>
        <form>
          <input
            value={username}
            name="username"
            type="text"
            placeholder="Username"
            onChange={this.handleInputChange}
            maxLength="32"
            minLength="4"
            required
          />
          <input
            value={password}
            name="password"
            type="password"
            placeholder="Password"
            onChange={this.handleInputChange}
            maxLength="32"
            minLength="4"
            required
          />
          <br />
          <button onClick={(e) => this.handleSubmit(e)} type="submit">Sign In</button>
        </form>
        {this.renderAlert()}
      </div>
    );
  };
}

export default SignIn;