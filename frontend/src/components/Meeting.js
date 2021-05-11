import React from 'react'
import { Container } from 'reactstrap'
import { PageLayout } from '../layouts'
import { useAuth } from '../providers'

export const Meeting = () => {
  const { user } = useAuth()

  return (
    <PageLayout>
      <Container>
        <h3>
          Hello{user ? `, ${user.name} ${user.surname}` : ''}. Let's study
          today!
        </h3>
      </Container>
    </PageLayout>
  )
}
