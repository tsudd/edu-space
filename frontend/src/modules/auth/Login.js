import React, { useState } from 'react'
import { useHistory } from 'react-router-dom'
import { useAuth } from '../../providers'
import {
  Card,
  Col,
  CardBody,
  CardTitle,
  Button,
  Form,
  FormGroup,
  Label,
  Input,
} from 'reactstrap'
import { ACCESS_TOKEN_NAME, API_BASE_URL } from '../../constants/urls'
import { useLogger } from '../../providers'
import { PageLayout } from '../../layouts'

export const Login = (props) => {
  let history = useHistory()

  const { setAuth, setUser, setToken } = useAuth()

  const { showError } = useLogger()

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

  const sendDetailsToServer = async () => {
    if (state.username.length && state.password.length) {
      const payload = {
        username: state.username,
        password: state.password,
      }
      try {
        const reps = await fetch(API_BASE_URL + 'auth/login', {
          method: 'POST',
          body: JSON.stringify(payload),
          headers: {
            'Content-Type': 'application/json',
          },
        })
        if (!reps.ok) {
          showError('Something went wrong.')
          return
        }
        const json = await reps.json()
        if (json.token) {
          localStorage.setItem(ACCESS_TOKEN_NAME, json.token)
          setAuth(true)
          setUser(json.account)
          setToken(json.token)
          redirectToHome()
        } else {
          showError('Please enter valid username and password')
        }
      } catch (e) {
        console.error('Ошибка:', e)
      }
    } else {
      showError('Please enter valid username and password')
    }
  }

  const handleSubmitClick = async (e) => {
    e.preventDefault()
    void (await sendDetailsToServer())
  }

  const redirectToHome = () => {
    history.push('/')
  }

  return (
    // <div className="col-md-6 mx-auto mt-5">
    <PageLayout showSubjectList={false}>
      <Col md="4" className="mx-auto mt-5">
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
                  name="pass"
                  id="password"
                  placeholder="Enter password"
                  value={state.password}
                  onChange={handleChange}
                />
              </FormGroup>
              <FormGroup>
                <Button
                  type="submit"
                  color="primary"
                  onClick={handleSubmitClick}
                >
                  Login
                </Button>
              </FormGroup>
            </Form>
          </CardBody>
        </Card>
      </Col>
    </PageLayout>
  )
}
