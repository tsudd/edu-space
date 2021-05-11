import React, { useEffect, useState } from 'react'
import {
  BrowserRouter,
  Switch,
  Route,
  Redirect,
  useLocation,
  useHistory,
} from 'react-router-dom'
import { useAuth } from '../providers/AuthProvider'
import {
  Card,
  Col,
  CardBody,
  CardTitle,
  CardSubtitle,
  Button,
  Form,
  FormGroup,
  Label,
  Input,
} from 'reactstrap'
import { ACCESS_TOKEN_NAME, API_BASE_URL } from '../constants/urls'

export const Login = (props) => {
  const { setAuth, auth, setToken, setUser } = useAuth()

  if (auth) return <Redirect to="/" />

  let history = useHistory()

  const [state, setState] = useState({
    username: '',
    password: '',
  })

  const handleChange = (e) => {
    const { id, value } = e.target
    setState((prevState) => ({
      ...prevState,
      [id]: value,
    }))
  }

  const sendDetailsToServer = () => {
    if (state.username.length && state.password.length) {
      const payload = {
        username: state.username,
        password: state.password,
      }
      const getResp = async () => {
        try {
          const reps = await fetch(API_BASE_URL + 'auth/login', {
            method: 'POST',
            body: JSON.stringify(payload),
            headers: {
              'Content-Type': 'application/json',
            },
          })
          if (!reps.ok) {
            props.showError('Something went wrong.')
          }
          const json = await reps.json()
          if (json.token) {
            console.log('Succesful loging with token ', json.token)
            localStorage.setItem(ACCESS_TOKEN_NAME, json.token)
            setToken(json.token)
            setUser(json.account)
            redirectToHome()
            props.showError(null)
          } else {
            props.showError('Please enter valid username and password')
          }
        } catch (e) {
          console.error('Ошибка:', e)
        }
      }
      void getResp()
    } else {
      props.showError('Please enter valid username and password')
    }
  }

  const handleSubmitClick = (e) => {
    e.preventDefault()
    sendDetailsToServer()
  }

  const redirectToHome = () => {
    history.push('/')
  }

  return (
    // <div className="col-md-6 mx-auto mt-5">
    <Col md="3" className="mx-auto mt-5">
      <Card>
        <CardBody>
          <CardTitle tag="h5">Login</CardTitle>
          <Form>
            <FormGroup>
              <Label for="username">Username</Label>
              <Input
                type="text"
                name="name"
                id="username"
                onChange={handleChange}
                placeholder="Enter ID"
                value={state.username}
              />
            </FormGroup>
            <FormGroup>
              <Label for="password">Password</Label>
              <Input
                type="password"
                name="password"
                id="password"
                placeholder="Enter password"
                value={state.password}
                onChange={handleChange}
              />
            </FormGroup>
            <FormGroup>
              <Button type="submit" color="primary" onClick={handleSubmitClick}>
                Login
              </Button>
            </FormGroup>
          </Form>
        </CardBody>
      </Card>
    </Col>
  )
}
