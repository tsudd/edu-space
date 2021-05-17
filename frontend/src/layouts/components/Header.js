import React, { useState, useEffect } from 'react'
import { Nav, Navbar, NavbarBrand, NavItem } from 'reactstrap'
import { Link, useHistory } from 'react-router-dom'
import { useAuth } from '../../providers'
import { ACCESS_TOKEN_NAME, TASK_CREATION_URL } from '../../constants/urls'

export const Header = (props) => {
  const { auth, setAuth, user, setUser, setToken } = useAuth()
  let logout
  let history = useHistory()
  let staff_links

  const handleLogout = () => {
    localStorage.removeItem(ACCESS_TOKEN_NAME)
    setAuth(false)
    setUser(null)
    setToken(null)
  }

  if (auth) {
    logout = (
      <NavItem>
        <Link to="/login" onClick={handleLogout}>
          Logout
        </Link>
      </NavItem>
    )
  }
  if (auth && user && user.is_staff) {
    staff_links = (
      <NavItem>
        <Link to={TASK_CREATION_URL}>Create task</Link>
      </NavItem>
    )
  }

  return (
    <div>
      <Navbar color="light" light expand="md">
        <div className="container">
          <Link className="mr-auto navbar-brand" to="/">
            Edu<strong>Space</strong>
          </Link>
          <Nav navbar>
            {logout}
            {staff_links}
          </Nav>
        </div>
      </Navbar>
    </div>
  )
}
