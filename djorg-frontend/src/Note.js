import React from 'react'

class Note extends React.Component {
  render() {
    return (
      <div>
        {this.props.title}
        <br />
        {this.props.content}
        <hr />
      </div>
    )
  }
}

export default Note;