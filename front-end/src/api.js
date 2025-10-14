import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api',
  withCredentials: true
});

// Auth endpoints
export const login = (username, password) =>
  API.post('/auth/login', { username, password });

export const logout = () =>
  API.post('/auth/logout');

export const whoami = () =>
  API.get('/auth/whoami');

// Products
export const getProducts = (query = '') =>
  API.get(`/products?q=${query}`);

// Sales
export const createSale = (data) =>
  API.post('/sales', data);
