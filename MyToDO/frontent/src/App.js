import React from 'react';
import axios from 'axios';
import UserList from './components/UserList.js';
import ProjectList from './components/ProjectList.js';
import TODOList from './components/TODOList.js';
import LoginForm from './components/LoginForm.js';
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'



const NotFound = () => {
    var location = useLocation()

    return (
        <div>
            Page "{location.pathname}" not found
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'users': [],
            'projects':[],
            'todos':[],
            'token':''
        }
    }

    obtainAuthToken(login, password){
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {'username': login, 'password': password})
            .then(responce => {
                let token = responce.data.token
                console.log(token)
                localStorage.setItem('tokem', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }
    getData() {
        let headers = this.getHeaders()
        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(error => {
                this.setState({
                    'users': []
                })
                console.log(error)
            })
        axios
            .get('http://127.0.0.1:8000/api/project/', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => {
                this.setState({
                    'projects': []
                })
                console.log(error)
            })
        axios
            .get('http://127.0.0.1:8000/api/todo/',{headers})
            .then(response => {
                const todos = response.data.results
                this.setState({
                    'todos': todos
                })
            })
            .catch(error => {
                this.setState({
                    'todos': []
                })
                console.log(error)
            })
    }
//    ComponentMenu(){}
//    ComponentFooter(){}

    render(){
        return(
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Users</Link></li>
                        <li><Link to='/Project'>Projects</Link></li>
                        <li><Link to='/TODO'>TODO</Link></li>
                        <li>
                        { this.isAuth() ? <button onClick={()=>this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element = {<UserList users={this.state.users} />} />
                        <Route exact path='/login' element = {<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />
                        <Route exact path='/Project' element = {<ProjectList projects={this.state.projects} />} />
                        <Route exact path='/User' element = {<Navigate to='/' />} />
                        <Route exact path='/TODO' element = {<TODOList todos={this.state.todos}/>}  />
                        <Route path='*' element = {<NotFound />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}


export default App;
