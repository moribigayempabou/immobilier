# -*- coding: utf-8 -*-

from odoo import models, fields, api

class immobilier_maison(models.Model):
      _name = 'immobilier.maison'
      _description = 'Maison'
      
      reference = fields.Char(string='Référence',required=True)
      typem = fields.Selection([('F1','Type F1'),('F2','Type F2'),('F3','Type F3'),('F4','Type F4')],string='Type de maison',required=True) 
      ville = fields.Char(string ='Ville')
      quartier = fields.Char(string = 'Quartier')
      destination = fields.Selection([('location','Location'),('vente','Vente')],string='Destination',required=True) 
      prixlocation = fields.Float(string='Prix location', digits=(16,0))
      prixvente = fields.Float(string='Prix vente', digits=(16,0))
      geoloc = fields.Text(string='Géolocalisation')
      notes = fields.Html(string='Notes')

class immobilier_client(models.Model):
      _name = 'immobilier.client'
      _description = 'Client'
      
      nom = fields.Char(string='Nom et prénom',required=True)
      datenaiss = fields.Date(string='Date de naissance')
      contact = fields.Char(string='Contact')

class immobilier_location(models.Model):
      _name = 'immobilier.location'
      _description = 'Location'  

      idclient = fields.Many2one('immobilier.client',string='Client')  
      idmaison = fields.Many2one('immobilier.maison', string='Maison')
      datedebut = fields.Date('Date de début')  
      datefin = fields.Date('Date de fin')  
      prix = fields.Float('Prix',related='idmaison.prixlocation')
      periodicite = fields.Selection([('mois','Mensuel'),('trimestre','Trimestriel'),('semestre','Semestriel'),('annee','Annuel')],string='Périodicité')

class immobilier_vente(models.Model):
      _name = 'immobilier.vente'
      _description = 'Vente'  

      idclient = fields.Many2one('immobilier.client',string='Client')  
      idmaison = fields.Many2one('immobilier.maison', string='Maison')
      dateacq = fields.Date('Date d\'acquisition')   
      prix = fields.Float('Prix',related='idmaison.prixvente')
      periodicite = fields.Selection([('mois','Mensuel'),('trimestre','Trimestriel'),('semestre','Semestriel'),('annee','Annuel')],string='Périodicité')

class immobilier_versement(models.Model):
      _name = 'immobilier.versement'
      _description = 'Versement'
      
      datevers = fields.Date('Date')
      montant = fields.Float('Montant', digits=(16,0))
      nomremettant = fields.Char('Nom du remettant')
      idlocation = fields.Many2one('immobilier.location',string='Location')
      idvente = fields.Many2one('immobilier.vente',string='Vente')
      

