import React, { useEffect, useState } from 'react'
import { useHistory } from 'react-router'
import { Col, Container, Row } from 'reactstrap'
import {
  ACCESS_TOKEN_NAME,
  API_AUTH_ACCOUNT,
  API_BASE_URL,
  API_SUBJECTS,
} from '../constants/urls'
import { PageLayout } from '../layouts/PageLayout'
import { useAuth } from '../providers'

export const Main = () => {
  let history = useHistory()

  const redirectToLogin = () => {
    history.push('/login')
  }

  const { token } = useAuth()

  useEffect(() => {
    const getUser = async () => {
      try {
        const resp = await fetch(API_BASE_URL + API_AUTH_ACCOUNT, {
          method: 'GET',
          headers: {
            Authorization: ACCESS_TOKEN_NAME + ' ' + token,
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
    <PageLayout>
      <Container className="mt-5">
        <h1>Main</h1>
      </Container>
    </PageLayout>
  )
}
