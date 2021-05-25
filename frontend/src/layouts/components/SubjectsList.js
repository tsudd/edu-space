import React from 'react'
import { Link } from 'react-router-dom'
import { CardBody, CardTitle, Container, Card, CardSubtitle } from 'reactstrap'
import { useSubjects } from '../../providers/SubjectsProvider'

export const SubjectList = () => {
  const { subjects } = useSubjects()

  return (
    <Container fluid="md">
      {subjects?.map((sub) => (
        <Link to={`/subject/${sub.id}`} key={sub.id}>
          <Card>
            <CardBody>
              <CardTitle tag="h5">{sub.name}</CardTitle>
              <CardSubtitle tag="h6" className="mb-2 text-muted">
                {sub.description}
              </CardSubtitle>
            </CardBody>
          </Card>
        </Link>
      ))}
    </Container>
  )
}
