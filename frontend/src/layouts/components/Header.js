import React from 'react'
import { Nav, Navbar, NavbarBrand, NavItem } from 'reactstrap'
import { Link } from 'react-router-dom'
import { useAuth } from '../../providers'
import { ACCESS_TOKEN_NAME } from '../../constants/urls'

export const Header = (props) => {
  const { auth, setAuth } = useAuth()
  let logout

  const handleLogout = () => {
    localStorage.removeItem(ACCESS_TOKEN_NAME)
    setAuth(false)
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

  return (
    <div>
      <Navbar color="light" light expand="md">
        <div className="container">
          <NavbarBrand className="mr-auto" href="/">
            Edu<strong>Space</strong>
          </NavbarBrand>
          <Nav navbar>{logout}</Nav>
        </div>
      </Navbar>
    </div>
  )
}
