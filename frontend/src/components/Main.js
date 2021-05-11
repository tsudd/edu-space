import React, { useEffect } from 'react'
import { useHistory } from 'react-router'
import { Col, Container, Row } from 'reactstrap'
import { ACCESS_TOKEN_NAME, API_BASE_URL } from '../constants/urls'

export const Main = () => {
  const history = useHistory()

  const redirectToLogin = () => {
    history.push('/login')
  }

  useEffect(() => {
    const getUser = async () => {
      try {
        const resp = await fetch(API_BASE_URL + 'auth/account', {
          method: 'GET',
          headers: {
            Authorization:
              ACCESS_TOKEN_NAME + ' ' + localStorage.getItem(ACCESS_TOKEN_NAME),
          },
        })
        if (!resp.ok) {
          redirectToLogin()
        }
      } catch (e) {
        redirectToLogin()
      }
    }
    void getUser()
  })

  return (
    <Container className="mt-5">
      <Row>
        <Col></Col>
        <Col></Col>
        <Col></Col>
      </Row>
    </Container>
  )
}
