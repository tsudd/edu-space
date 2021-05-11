import React, { useState } from 'react'
import { Col, Container, Row } from 'reactstrap'
import { Header, SubjectList } from './components'
import { ACCESS_TOKEN_NAME } from '../constants/urls'

export const PageLayout = ({ children, showSubjectList = true }) => {
  return (
    <>
      <Header />
      <Container>
        <Row>
          {showSubjectList && (
            <Col>
              <SubjectList />
            </Col>
          )}
          <Col>{children}</Col>
        </Row>
      </Container>
    </>
  )
}
