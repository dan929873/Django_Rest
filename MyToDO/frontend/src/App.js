import React from 'react';
import axios from 'axios';
import UserList from './components/UserList.js';
import ProjectList from './components/ProjectList.js';
import TODOList from './components/TODOList.js';
//import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'


//const NotFound = () => {
//    var location = useLocation()
//
//    return (
//        <div>
//            Page "{location.pathname}" not found
//        </div>
//    )
//}


class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'users': [],
            'projects':[],
            'todos':[]
        }
    }
    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/project/')
            .then(response => {
                const projects = response.data
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data
                this.setState({
                    'todos': todos
                })
            })
            .catch(error => console.log(error))
    }
//    ComponentMenu(){}
//    ComponentFooter(){}

    render(){
        return(
            <div className="App">
                <UserList users={this.state.users}/>
                <ProjectList projects={this.state.projects}/>
                <TODOList todos={this.state.todos}/>
            </div>
        )
    }
}


export default App;
