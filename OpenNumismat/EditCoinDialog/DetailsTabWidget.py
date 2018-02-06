from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *

from OpenNumismat.EditCoinDialog.FormItems import DoubleValidator
from OpenNumismat.EditCoinDialog.BaseFormLayout import BaseFormLayout, BaseFormGroupBox, ImageFormLayout
from OpenNumismat.EditCoinDialog.BaseFormLayout import DesignFormLayout, FormItem
from OpenNumismat.Collection.CollectionFields import FieldTypes as Type
from OpenNumismat.Tools.Converters import numberWithFraction, stringToMoney
from OpenNumismat.Settings import Settings

COIN_PAGE = {
    'page': "Coin",
    'parts': [
        {
            'title': "Main details",
            'type': 'GroupBox',
            'items': [
                'title',
                'region',
                'country',
                'period',
                'ruler',
                ['value', 'unit'],
                'year',
                ['mintmark', 'mint'],
                'type',
                'series',
                'subjectshort'
            ]
        },
        {'type': 'Stretch'},
        {
            'title': "State",
            'type': 'GroupBox',
            'items': [
                ['status', 'grade'],
                ['quantity', 'format'],
                'condition',
                ['storage', 'barcode'],
                'defect',
                'features'
            ]
        }
    ]
}

PARAMETERS_PAGE = {
    'page': "Parameters",
    'parts': [
        {
            'title': "Parameters",
            'type': 'GroupBox',
            'items': [
                'material',
                ['fineness', 'weight'],
                ['diameter', 'thickness'],
                'shape',
                'obvrev'
            ]
        },
        {'type': 'Stretch'},
        {
            'title': "Minting",
            'type': 'GroupBox',
            'items': [
                ['issuedate', 'mintage'],
                'dateemis',
                'quality'
            ]
        },
        {
            'type': 'Layout',
            'items': [
                'note'
            ]
        }
    ]
}

DESIGN_PAGE = {
    'page': "Design",
    'parts': [
        {
            'title': "Obverse",
            'type': 'DesignFormLayout',
            'items': [
                'obverseimg',
                'obversedesign',
                'obversedesigner',
                'obverseengraver',
                'obversecolor'
            ]
        },
        {
            'title': "Reverse",
            'type': 'DesignFormLayout',
            'items': [
                'reverseimg',
                'reversedesign',
                'reversedesigner',
                'reverseengraver',
                'reversecolor'
            ]
        },
        {'type': 'Stretch'},
        {
            'title': "Edge",
            'type': 'DesignFormLayout',
            'items': [
                'edgeimg',
                'edge',
                'edgelabel'
            ]
        },
        {
            'type': 'Layout',
            'items': [
                'subject'
            ]
        }
    ]
}


class DetailsTabWidget(QTabWidget):
    Direction = QBoxLayout.LeftToRight
    Stretch = 'stretch item'

    def __init__(self, model, parent=None):
        super().__init__(parent)

        self.model = model
        self.reference = model.reference

        self.createItems()
        self.createPages()

    def createPages(self):
        self.createCoinPage()
        self.createTrafficPage()
        self.createParametersPage()
        self.createDesignPage()
        self.createClassificationPage()

    def createPage(self, settings):
        title = settings['page']
        parts = []
        for part in settings['parts']:
            if part['type'] == 'Stretch':
                parts.append(self.Stretch)
            elif part['type'] == 'GroupBox':
                layout = BaseFormGroupBox(part['title'])

                for item in part['items']:
                    if isinstance(item, str):
                        layout.addRow(self.items[item])
                    else:
                        item1 = item[0]
                        item2 = item[1]
                        layout.addRow(self.items[item1], self.items[item2])

                parts.append(layout)
            elif part['type'] == 'DesignFormLayout':
                layout = DesignFormLayout(part['title'])

                for item in part['items']:
                    if isinstance(item, str):
                        if item in ('obverseimg', 'reverseimg', 'edgeimg', 'varietyimg'):
                            if isinstance(self, FormDetailsTabWidget):
                                layout.addImage(self.items[item])
                        else:
                            layout.addRow(self.items[item])
                    else:
                        item1 = item[0]
                        item2 = item[1]
                        layout.addRow(self.items[item1], self.items[item2])

                parts.append(layout)
            elif part['type'] == 'Layout':
                layout = BaseFormLayout()

                for item in part['items']:
                    layout.addRow(self.items[item])

                parts.append(layout)

        self.addTabPage(title, parts)

    def createCoinPage(self):
        self.createPage(COIN_PAGE)
        self.items['status'].widget().currentIndexChanged.connect(self.indexChangedState)

    def createTrafficPage(self):
        self.oldTrafficIndex = 0
        parts = self._createTrafficParts(self.oldTrafficIndex)
        title = QApplication.translate('DetailsTabWidget', "Market")
        self.addTabPage(title, parts)

    def createParametersPage(self):
        self.createPage(PARAMETERS_PAGE)

    def createDesignPage(self):
        self.createPage(DESIGN_PAGE)

    def createClassificationPage(self):
        catalogue = self.catalogueLayout()
        rarity = self.rarityLayout()
        price = self.priceLayout()
        variation = self.variationLayout()
        url = self.urlLayout()

        title = QApplication.translate('DetailsTabWidget', "Classification")
        self.addTabPage(title, [catalogue, rarity, price, self.Stretch,
                                variation, url])

    def _layoutToWidget(self, layout):
        widget = QWidget(self)
        widget.setLayout(layout)
        return widget

    def createTabPage(self, parts):
        # Remove all empty parts
        for part in parts:
            if isinstance(part, BaseFormGroupBox):
                if part.isEmpty():
                    parts.remove(part)

        if self.Direction == QBoxLayout.LeftToRight:
            newParts = []
            layout = QVBoxLayout()
            stretchNeeded = True
            count = 0
            for part in parts:
                if part == self.Stretch:
                    if count > 0:
                        newParts.append(layout)
                        if stretchNeeded:
                            layout.insertStretch(-1)
                        layout = QVBoxLayout()
                    stretchNeeded = True
                    count = 0
                else:
                    if isinstance(part, QWidget):
                        layout.addWidget(part)
                        if part.sizePolicy().verticalPolicy() == QSizePolicy.Preferred:
                            stretchNeeded = False
                    else:
                        layout.addLayout(part)
                    count += 1
            if count > 0:
                newParts.append(layout)
                if stretchNeeded:
                    layout.insertStretch(-1)
            parts = newParts
        else:
            for part in parts:
                if part == self.Stretch:
                    parts.remove(part)

        pageLayout = QBoxLayout(self.Direction, self)
        # Fill layout with it's parts
        stretchNeeded = True
        for part in parts:
            if isinstance(part, QWidget):
                pageLayout.addWidget(part)
                if part.sizePolicy().verticalPolicy() == QSizePolicy.Preferred:
                    stretchNeeded = False
            else:
                pageLayout.addLayout(part)
                if isinstance(part, ImageFormLayout):
                    stretchNeeded = False

        if self.Direction == QBoxLayout.TopToBottom and stretchNeeded:
            pageLayout.insertStretch(-1)

        return self._layoutToWidget(pageLayout)

    def addTabPage(self, title, parts):
        page = self.createTabPage(parts)
        index = self.addTab(page, title)

    def addItem(self, field):
        # Skip image fields for not a form
        if field.type in Type.ImageTypes:
            return

        item = FormItem(field.name, field.title, field.type | Type.Disabled,
                        reference=self.reference)
        if not field.enabled:
            item.setHidden()
        self.items[field.name] = item

    def createItems(self):
        self.items = {}

        fields = self.model.fields
        for field in fields:
            if field not in fields.systemFields:
                self.addItem(field)

    def fillItems(self, record):
        if not record.isEmpty():
            # Fields with commission dependent on status field and should be
            # filled after it and in right order
            ordered_item_keys = ('status', 'payprice', 'totalpayprice',
                                 'saleprice', 'totalsaleprice',
                                 'region', 'country')
            for key in ordered_item_keys:
                if key in self.items:
                    item = self.items[key]
                    self._fillItem(record, item)

            for item in self.items.values():
                if item.field() in ordered_item_keys:
                    continue

                self._fillItem(record, item)

    def _fillItem(self, record, item):
        if not record.isNull(item.field()):
            value = record.value(item.field())
            item.setValue(value)
        else:
            item.widget().clear()

    def clear(self):
        for item in self.items.values():
            item.widget().clear()

    def emptyMarketLayout(self):
        text = QApplication.translate('DetailsTabWidget',
                "Nothing to show. Change the coin status on previous tab")
        label = QLabel(text)
        layout = QHBoxLayout()
        layout.addWidget(label)

        return layout

    def payLayout(self):
        title = QApplication.translate('DetailsTabWidget', "Buy")
        layout = BaseFormGroupBox(title)

        layout.addRow(self.items['paydate'], self.items['payprice'])

        # Add auxiliary field
        item = self.addPayCommission()

        layout.addRow(self.items['totalpayprice'], item)
        layout.addRow(self.items['saller'])
        layout.addRow(self.items['payplace'])
        layout.addRow(self.items['payinfo'])

        return layout

    def saleLayout(self):
        title = QApplication.translate('DetailsTabWidget', "Sale")
        layout = BaseFormGroupBox(title)

        layout.addRow(self.items['saledate'], self.items['saleprice'])

        # Add auxiliary field
        item = self.addSaleCommission()
        layout.addRow(self.items['totalsaleprice'], item)

        layout.addRow(self.items['buyer'])
        layout.addRow(self.items['saleplace'])
        layout.addRow(self.items['saleinfo'])

        return layout

    def passLayout(self):
        title = QApplication.translate('DetailsTabWidget', "Pass")
        layout = BaseFormGroupBox(title)

        layout.addRow(self.items['saledate'], self.items['saleprice'])

        # Add auxiliary field
        item = self.addPayCommission()
        layout.addRow(self.items['totalpayprice'], item)
        self.items['saleprice'].widget().textChanged.connect(self.items['payprice'].widget().setText)

        # Add auxiliary field
        item = self.addSaleCommission()
        layout.addRow(self.items['totalsaleprice'], item)

        layout.addRow(self.items['saller'])
        layout.addRow(self.items['buyer'])
        layout.addRow(self.items['saleplace'])
        layout.addRow(self.items['saleinfo'])

        return layout

    def rarityLayout(self):
        layout = BaseFormLayout()

        item = self.items['rarity']
        layout.addHalfRow(item)
        item.widget().setSizePolicy(QSizePolicy.Preferred,
                                    QSizePolicy.Fixed)

        return layout

    def catalogueLayout(self):
        title = QApplication.translate('DetailsTabWidget', "Catalogue")
        layout = BaseFormGroupBox(title)

        layout.addRow(self.items['catalognum1'], self.items['catalognum2'])
        layout.addRow(self.items['catalognum3'], self.items['catalognum4'])

        return layout

    def priceLayout(self):
        title = QApplication.translate('DetailsTabWidget', "Price")
        layout = BaseFormGroupBox(title)

        layout.addRow(self.items['price4'], self.items['price3'])
        layout.addRow(self.items['price2'], self.items['price1'])

        return layout

    def variationLayout(self):
        title = QApplication.translate('DetailsTabWidget', "Variation")
        layout = BaseFormGroupBox(title)

        layout.addRow(self.items['variety'])
        item = self.items['varietydesc']
        layout.addRow(item)
        item.widget().setSizePolicy(QSizePolicy.Preferred,
                                    QSizePolicy.Minimum)
        layout.addRow(self.items['obversevar'], self.items['reversevar'])
        layout.addHalfRow(self.items['edgevar'])

        return layout

    def urlLayout(self):
        layout = BaseFormLayout()
        layout.setAlignment(Qt.AlignTop)

        layout.addRow(self.items['url'])

        return layout

    def _createTrafficParts(self, index=0):
        stretch_widget = QWidget()
        stretch_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        pageParts = []
        if index == 1:
            pass_ = self.passLayout()
            pageParts.extend([pass_, self.Stretch, stretch_widget])
        elif index == 2:
            pay = self.payLayout()
            pageParts.extend([pay, self.Stretch, stretch_widget])
        elif index == 3:
            pay = self.payLayout()
            pageParts.extend([pay, self.Stretch, stretch_widget])
        elif index == 4:
            pay = self.payLayout()
            sale = self.saleLayout()
            pageParts.extend([pay, self.Stretch, sale])
        elif index == 5:
            pay = self.payLayout()
            pageParts.extend([pay, self.Stretch, stretch_widget])
        else:
            layout = self.emptyMarketLayout()
            pageParts.append(layout)

        self.oldTrafficIndex = index

        return pageParts

    def indexChangedState(self, index):
        pageIndex = self.currentIndex()

        self.removeTab(1)
        pageParts = self._createTrafficParts(index)
        page = self.createTabPage(pageParts)

        title = QApplication.translate('DetailsTabWidget', "Market")
        self.insertTab(1, page, title)
        self.setCurrentIndex(pageIndex)

    def addPayCommission(self):
        title = QApplication.translate('DetailsTabWidget', "Commission")
        self.payComission = FormItem(None, title, Type.Money | Type.Disabled)

        self.items['payprice'].widget().textChanged.connect(self.payPriceChanged)
        self.items['totalpayprice'].widget().textChanged.connect(self.payPriceChanged)

        return self.payComission

    def payPriceChanged(self, text):
        totalPriceValue = self.items['totalpayprice'].value()
        if totalPriceValue:
            price = textToFloat(self.items['payprice'].value())
            totalPrice = textToFloat(totalPriceValue)
            self.payComission.widget().setText(floatToText(totalPrice - price))
        else:
            self.payComission.widget().setText('')

    def addSaleCommission(self):
        title = QApplication.translate('DetailsTabWidget', "Commission")
        self.saleComission = FormItem(None, title, Type.Money | Type.Disabled)

        self.items['saleprice'].widget().textChanged.connect(self.salePriceChanged)
        self.items['totalsaleprice'].widget().textChanged.connect(self.salePriceChanged)

        return self.saleComission

    def salePriceChanged(self, text):
        totalPriceValue = self.items['totalsaleprice'].value()
        if totalPriceValue:
            price = textToFloat(self.items['saleprice'].value())
            totalPrice = textToFloat(totalPriceValue)
            self.saleComission.widget().setText(floatToText(price - totalPrice))
        else:
            self.saleComission.widget().setText('')


class FormDetailsTabWidget(DetailsTabWidget):
    Direction = QBoxLayout.TopToBottom

    def __init__(self, model, parent=None, usedFields=None):
        self.usedFields = usedFields
        self.settings = Settings()

        super().__init__(model, parent)

    def createPages(self):
        self.createCoinPage()
        self.createTrafficPage()
        self.createParametersPage()
        self.createDesignPage()
        self.createClassificationPage()
        self.createImagePage()

    def createImagePage(self):
        images = self.imagesLayout()
        self.addTabPage(self.tr("Images"), [images, ])

    def addItem(self, field):
        checkable = 0
        if self.usedFields:
            checkable = Type.Checkable

        section = None
        if self.reference:
            section = self.reference.section(field.name)

        item = FormItem(field.name, field.title, field.type | checkable,
                        section=section)
        if not field.enabled:
            item.setHidden()
        self.items[field.name] = item

    def createItems(self):
        super().createItems()

        if self.reference:
            if self.reference.section('country'):
                country = self.items['country'].widget()
                if self.reference.section('region'):
                    region = self.items['region'].widget()
                    region.addDependent(country)
                if self.reference.section('period'):
                    country.addDependent(self.items['period'].widget())
                if self.reference.section('ruler'):
                    country.addDependent(self.items['ruler'].widget())
                if self.reference.section('unit'):
                    country.addDependent(self.items['unit'].widget())
                if self.reference.section('mint'):
                    country.addDependent(self.items['mint'].widget())
                if self.reference.section('series'):
                    country.addDependent(self.items['series'].widget())

        image_fields = ('obverseimg', 'reverseimg', 'edgeimg', 'varietyimg',
                        'photo1', 'photo2', 'photo3', 'photo4')
        for image_field_src in image_fields:
            for image_field_dst in image_fields:
                if image_field_dst != image_field_src:
                    if not self.items[image_field_dst].isHidden():
                        src = self.items[image_field_src].widget()
                        dst = self.items[image_field_dst].widget()
                        title = self.items[image_field_dst].title()
                        src.connectExchangeAct(dst, title)

    def fillItems(self, record):
        super().fillItems(record)

        if self.usedFields:
            for item in self.items.values():
                if self.usedFields[record.indexOf(item.field())]:
                    item.label().setCheckState(Qt.Checked)

        image_fields = ('obverseimg', 'reverseimg', 'edgeimg', 'varietyimg',
                        'photo1', 'photo2', 'photo3', 'photo4')
        for image_field in image_fields:
            title = record.value(image_field + '_title')
            if title:
                self.items[image_field].widget().setTitle(title)

    def mainDetailsLayout(self):
        layout = BaseFormGroupBox(self.tr("Main details"))
        layout.layout.columnCount = 6

        btn = QPushButton(self.tr("Generate"))
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.clicked.connect(self.clickGenerateTitle)
        layout.addRow(self.items['title'], btn)

        layout.addRow(self.items['region'])
        layout.addRow(self.items['country'])
        layout.addRow(self.items['period'])
        layout.addRow(self.items['ruler'])
        layout.addRow(self.items['value'], self.items['unit'])
        layout.addRow(self.items['year'])
        layout.addRow(self.items['mintmark'], self.items['mint'])
        layout.addRow(self.items['type'])
        layout.addRow(self.items['series'])
        layout.addRow(self.items['subjectshort'])

        return layout

    def variationLayout(self):
        layout = DesignFormLayout(self.tr("Variation"))

        layout.addImage(self.items['varietyimg'], 2)
        layout.addRow(self.items['variety'])
        item = self.items['varietydesc']
        layout.addRow(item)
        item.widget().setSizePolicy(QSizePolicy.Preferred,
                                    QSizePolicy.Minimum)
        layout.addRow(self.items['obversevar'], self.items['reversevar'])
        layout.addHalfRow(self.items['edgevar'])

        return layout

    def imagesLayout(self):
        layout = ImageFormLayout()
        layout.addImages([self.items['photo1'], self.items['photo2'],
                          self.items['photo3'], self.items['photo4']])
        return layout

    def clickGenerateTitle(self):
        titleParts = []
        for key in ('value', 'unit', 'year', 'subjectshort',
                    'mintmark', 'variety'):
            value = self.items[key].value()
            if not isinstance(value, str):
                value = str(value)
            titlePart = value.strip()
            if titlePart:
                if key == 'unit':
                    titlePart = titlePart.lower()
                elif key == 'value':
                    titlePart, _ = numberWithFraction(titlePart, self.settings['convert_fraction'])
                elif key == 'subjectshort':
                    if len(titlePart.split()) > 1:
                        titlePart = '"%s"' % titlePart
                titleParts.append(titlePart)

        title = ' '.join(titleParts)
        self.items['title'].setValue(title)

    def _createTrafficParts(self, index=0):
        if self.oldTrafficIndex == 0:
            pass
        elif self.oldTrafficIndex == 1:
            self.items['payprice'].widget().textChanged.disconnect(self.payCommissionChanged)
            self.items['totalpayprice'].widget().textChanged.disconnect(self.payTotalPriceChanged)
            self.payCommission.textChanged.disconnect(self.payCommissionChanged)
            self.items['saleprice'].widget().textChanged.disconnect(self.saleCommissionChanged)
            self.items['totalsaleprice'].widget().textChanged.disconnect(self.saleTotalPriceChanged)
            self.saleCommission.textChanged.disconnect(self.saleCommissionChanged)
            self.items['saleprice'].widget().textChanged.disconnect(self.items['payprice'].widget().setText)
        elif self.oldTrafficIndex == 2:
            self.items['payprice'].widget().textChanged.disconnect(self.payCommissionChanged)
            self.items['totalpayprice'].widget().textChanged.disconnect(self.payTotalPriceChanged)
            self.payCommission.textChanged.disconnect(self.payCommissionChanged)
        elif self.oldTrafficIndex == 3:
            self.items['payprice'].widget().textChanged.disconnect(self.payCommissionChanged)
            self.items['totalpayprice'].widget().textChanged.disconnect(self.payTotalPriceChanged)
            self.payCommission.textChanged.disconnect(self.payCommissionChanged)
        elif self.oldTrafficIndex == 4:
            self.items['payprice'].widget().textChanged.disconnect(self.payCommissionChanged)
            self.items['totalpayprice'].widget().textChanged.disconnect(self.payTotalPriceChanged)
            self.payCommission.textChanged.disconnect(self.payCommissionChanged)
            self.items['saleprice'].widget().textChanged.disconnect(self.saleCommissionChanged)
            self.items['totalsaleprice'].widget().textChanged.disconnect(self.saleTotalPriceChanged)
            self.saleCommission.textChanged.disconnect(self.saleCommissionChanged)
        elif self.oldTrafficIndex == 5:
            self.items['payprice'].widget().textChanged.disconnect(self.payCommissionChanged)
            self.items['totalpayprice'].widget().textChanged.disconnect(self.payTotalPriceChanged)
            self.payCommission.textChanged.disconnect(self.payCommissionChanged)
        elif self.oldTrafficIndex == 6:
            pass

        pageParts = super()._createTrafficParts(index)

        self.oldTrafficIndex = index

        return pageParts

    def addPayCommission(self):
        item = FormItem(None, self.tr("Commission"), Type.Money)
        self.payCommission = item.widget()
        self.payCommission.setToolTip(self.tr("Available format 12.5 or 10%"))

        validator = CommissionValidator(0, 9999999999, 2, self)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.payCommission.setValidator(validator)

        self.items['payprice'].widget().textChanged.connect(self.payCommissionChanged)
        self.payCommission.textChanged.connect(self.payCommissionChanged)
        self.items['totalpayprice'].widget().textChanged.connect(self.payTotalPriceChanged)

        return item

    def addSaleCommission(self):
        item = FormItem(None, self.tr("Commission"), Type.Money)
        self.saleCommission = item.widget()
        self.saleCommission.setToolTip(self.tr("Available format 12.5 or 10%"))

        validator = CommissionValidator(0, 9999999999, 2, self)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.saleCommission.setValidator(validator)

        self.items['saleprice'].widget().textChanged.connect(self.saleCommissionChanged)
        self.saleCommission.textChanged.connect(self.saleCommissionChanged)
        self.items['totalsaleprice'].widget().textChanged.connect(self.saleTotalPriceChanged)

        return item

    def payCommissionChanged(self, text):
        self.items['totalpayprice'].widget().textChanged.disconnect(self.payTotalPriceChanged)

        price = textToFloat(self.items['payprice'].value())
        text = self.payCommission.text().strip()
        if len(text) > 0 and text[-1] == '%':
            commission = price * textToFloat(text[0:-1]) / 100
        else:
            commission = textToFloat(text)
        self.items['totalpayprice'].widget().setText(floatToText(price + commission))

        self.items['totalpayprice'].widget().textChanged.connect(self.payTotalPriceChanged)

    def payTotalPriceChanged(self, text):
        self.payCommission.textChanged.disconnect(self.payCommissionChanged)

        if text:
            price = textToFloat(self.items['payprice'].value())
            totalPrice = textToFloat(self.items['totalpayprice'].value())
            self.payCommission.setText(floatToText(totalPrice - price))
        else:
            self.payCommission.clear()

        self.payCommission.textChanged.connect(self.payCommissionChanged)

    def saleCommissionChanged(self, text):
        self.items['totalsaleprice'].widget().textChanged.disconnect(self.saleTotalPriceChanged)

        price = textToFloat(self.items['saleprice'].value())
        text = self.saleCommission.text().strip()
        if len(text) > 0 and text[-1] == '%':
            commission = price * textToFloat(text[0:-1]) / 100
        else:
            commission = textToFloat(text)
        self.items['totalsaleprice'].widget().setText(floatToText(price - commission))

        self.items['totalsaleprice'].widget().textChanged.connect(self.saleTotalPriceChanged)

    def saleTotalPriceChanged(self, text):
        self.saleCommission.textChanged.disconnect(self.saleCommissionChanged)

        if text:
            price = textToFloat(self.items['saleprice'].value())
            totalPrice = textToFloat(self.items['totalsaleprice'].value())
            self.saleCommission.setText(floatToText(price - totalPrice))
        else:
            self.saleCommission.clear()

        self.saleCommission.textChanged.connect(self.saleCommissionChanged)


def textToFloat(text):
    if text:
        return stringToMoney(text)
    else:
        return 0


def floatToText(value):
    if value > 0:
        return str(int((value) * 100 + 0.5) / 100)
    else:
        return str(int((value) * 100 - 0.5) / 100)


# Reimplementing DoubleValidator for replace comma with dot and accept %
class CommissionValidator(DoubleValidator):
    def validate(self, input_, pos):
        hasPercent = False
        numericValue = input_
        if len(input_) > 0 and input_[-1] == '%':
            numericValue = input_[0:-1]  # trim percent sign
            hasPercent = True
        state, validatedValue, pos = super().validate(numericValue, pos)
        if hasPercent:
            validatedValue = validatedValue + '%'  # restore percent sign
        return state, validatedValue, pos
