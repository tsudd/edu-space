import React from 'react'
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
import { Formik } from 'formik'
import { useSubjects } from '../providers'
import { object, string } from 'yup'

const initialValues = {
  name: '',
  subject: '',
  description: '',
  deadline: '',
}

const validationSchema = object({
  name: string().required('Wrong name'),
  subject: string().required(),
  description: string().required(),
  deadline: string().required('Invalid date'),
})

export const TaskForm = ({
  submitFunc,
  formTitle = 'Task creation',
  submitTitle = 'Create',
  task = null,
}) => {
  const { subjects } = useSubjects()

  if (task) {
    initialValues.name = task.name
    initialValues.description = task.description
    initialValues.deadline = task.deadline
    initialValues.subject = task.subject
    // console.log(228, initialValues)
  }

  const onSubmit = submitFunc

  return (
    <Col md="9" className="mx-auto mt-5">
      <Card>
        <CardBody>
          <CardTitle tag="h5">{formTitle}</CardTitle>
          <Formik
            onSubmit={onSubmit}
            validationSchema={validationSchema}
            initialValues={initialValues}
          >
            {({
              values,
              errors,
              handleChange,
              handleSubmit,
              isSubmitting,
              handleBlur,
            }) => (
              <Form onSubmit={(e) => e.preventDefault()}>
                <FormGroup> 
                  <Label for="name">Task name</Label>
                  <Input
                    type="text"
                    name="name"
                    id="name"
                    onBlur={handleBlur}
                    invalid={!!errors.name}
                    value={values.name}
                    onChange={handleChange}
                    placeholder="Enter name"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Description</Label>
                  <Input
                    type="textarea"
                    name="description"
                    onBlur={handleBlur}
                    invalid={!!errors.description}
                    value={values.description}
                    id="description"
                    placeholder="Enter information here"
                    onChange={handleChange}
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="deadline">Deadline</Label>
                  <Input
                    type="date"
                    name="deadline"
                    onBlur={handleBlur}
                    invalid={!!errors.deadline}
                    value={values.deadline}
                    id="deadline"
                    onChange={handleChange}
                    placeholder="Choose date"
                  />
                  {errors.deadline && (
                    <Label for="deadline">{errors.deadline}</Label>
                  )}
                </FormGroup>
                <FormGroup>
                  <legend className="col-form-label col-sm-2">Subjects</legend>
                  <Col sm={10}>
                    {subjects?.map((sub) => (
                      <FormGroup check key={sub.id}>
                        <Label check>
                          <Input
                            type="radio"
                            name={'subject'}
                            value={sub.id}
                            onChange={handleChange}
                            onBlur={handleBlur}
                            invalid={!!errors.subject}
                          />{' '}
                          {sub.name} | {sub.description}
                        </Label>
                      </FormGroup>
                    ))}
                  </Col>
                </FormGroup>
                <FormGroup>
                  <Button
                    type="submit"
                    color="primary"
                    disabled={isSubmitting}
                    onClick={handleSubmit}
                  >
                    {submitTitle}
                  </Button>
                </FormGroup>
              </Form>
            )}
          </Formik>
        </CardBody>
      </Card>
    </Col>
  )
}
