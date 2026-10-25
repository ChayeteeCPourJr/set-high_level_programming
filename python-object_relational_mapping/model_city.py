#!/usr/bin/python3
"""Defines the City class linked to the cities table."""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """City class linked to the cities table."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
