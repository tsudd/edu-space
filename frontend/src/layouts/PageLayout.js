import React from 'react'
import { Col, Container, Row } from 'reactstrap'
import { Header, SubjectList } from './components'

export const PageLayout = ({ children, showSubjectList = true }) => {
  return (
    <>
      <Header />
      <Container fluid={true}>
        <Row>
          {showSubjectList && (
            <Col md="3">
              <SubjectList />
            </Col>
          )}
          <Col>{children}</Col>
        </Row>
      </Container>
    </>
  )
}
